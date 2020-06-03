import json
import math
import multiprocessing
import sys

import numpy
from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest

from api.ana_url import split_url
from chatsentiment.pos_neg_spm import predict_pos_neg
from download.chatlog import download
from models.highlight import Predict
from sentiment7.sentiment7 import predict_7sentiment
from settings.utils import api

sys.path.append('../')

app = Blueprint('predict', __name__, url_prefix='/api')


def posneg(comment, second, inc, url, returnDict):
    predict = numpy.transpose(
        [[s[1:-1] for s in second], predict_pos_neg(comment)])
    predict_per_unitsecond = {'pos': [], 'neg': []}
    poscnt = 0
    negcnt = 0
    x = inc
    for p in predict:
        if int(p[0]) > x:
            x += inc
            predict_per_unitsecond['pos'].append(poscnt)
            predict_per_unitsecond['neg'].append(negcnt)
            poscnt = 0
            negcnt = 0
        if int(p[1]) == 1:
            poscnt += 1
        elif int(p[1]) == 0:
            negcnt += 1
    returnDict['posneg'] = predict_per_unitsecond


def sentiment7(comment, second, inc, url, returnDict):
    predict = numpy.transpose(
        [[s[1:-1] for s in second], predict_7sentiment(comment)])
    predict_per_unitsecond = {
        'neutral': [],
        'joy': [],
        'love': [],
        'fear': [],
        'surprise': [],
        'sadness': [],
        'anger': []
    }
    x = inc
    neutral = 0
    joy = 0
    love = 0
    fear = 0
    surprise = 0
    sadness = 0
    anger = 0
    for p in predict:
        if int(p[0]) > x:
            x += inc
            predict_per_unitsecond['neutral'].append(neutral)
            predict_per_unitsecond['joy'].append(joy)
            predict_per_unitsecond['love'].append(love)
            predict_per_unitsecond['fear'].append(fear)
            predict_per_unitsecond['surprise'].append(surprise)
            predict_per_unitsecond['sadness'].append(sadness)
            predict_per_unitsecond['anger'].append(anger)
            neutral = 0
            joy = 0
            love = 0
            fear = 0
            surprise = 0
            sadness = 0
            anger = 0
        if p[1] == 'neutral':
            neutral += 1
        elif p[1] == 'joy':
            joy += 1
        elif p[1] == 'love':
            love += 1
        elif p[1] == 'fear':
            fear += 1
        elif p[1] == 'surprise':
            surprise += 1
        elif p[1] == 'sadness':
            sadness += 1
        elif p[1] == 'anger':
            anger += 1

    returnDict['sentiment7'] = predict_per_unitsecond


@app.route('/predict', methods=['GET'])
@api
def get_predict(data, db):
    manager = multiprocessing.Manager()
    returnDict = manager.dict()
    url = data['url']
    isURLValid = split_url(url)

    if not isURLValid:
        raise BadRequest

    query = db.query(Predict).filter(
        Predict.url == url,
    ).first()

    if query:
        return query.predict_json

    download(isURLValid[0], isURLValid[1])

    with open('./chatlog/{}_{}.txt'.format(isURLValid[0], isURLValid[1]), encoding='utf-8') as f:
        content = f.read().split('\n')

    second = []
    comment = []
    for i in range(0, len(content) - 1):
        splited_chat = content[i].split('\t')
        if len(splited_chat) < 3:
            continue
        second.append(splited_chat[0])
        comment.append(splited_chat[2])

    if len(second) < 1 or len(comment) < 1:
        raise BadRequest

    endSecond = int(second[-1][1:-1])

    if endSecond >= 100.0:
        inc = math.floor(endSecond / 100.0)
    else:
        inc = 1.0
    p1 = multiprocessing.Process(target=posneg, args=(comment, second, inc, url, returnDict))
    p2 = multiprocessing.Process(target=sentiment7, args=(comment, second, inc, url, returnDict))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    returnDict['bin'] = inc
    rst = json.dumps(returnDict.copy())
    new_predict = Predict(
        url=url,
        predict_json=rst,
    )
    db.add(new_predict)
    db.commit()
    return jsonify(rst)
