import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from settings.utils import api
from sentiment7.sentiment7 import predict
from werkzeug.exceptions import BadRequest
from api.ana_url import split_url
from download.chatlog import download
import math
from models.highlight import Predict7

app = Blueprint('predict7', __name__, url_prefix='/api')


@app.route('/predict7', methods=['GET'])
@api
def get_predict7(data, db):
    url = data['url']
    isURLValid = split_url(url)
    if not isURLValid:
        raise BadRequest
    query = db.query(Predict7).filter(
        Predict7.url == url,
    ).first()
    if query:
        return query.sentiment7_json
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
    p = predict(comment)
    if endSecond >= 100:
        x = math.ceil(endSecond / 100)
    else:
        x = 1
    temp = 0
    predict_per_unitsecond = {
        'neutral': [],
        'joy': [],
        'love': [],
        'fear': [],
        'surprise': [],
        'sadness': [],
        'anger': []}
    while temp < endSecond:
        neutral=0; joy=0; love=0; fear=0; surprise=0; sadness=0; anger=0
        for i in p[temp:temp + x]:
            if i == 'neutral':
                neutral += 1
            elif i == 'joy':
                joy += 1
            elif i == 'love':
                love += 1
            elif i == 'fear':
                fear += 1
            elif i == 'surprise':
                fear += 1
            elif i == 'sadness':
                sadness += 1
            elif i == 'anger':
                anger += 1
        predict_per_unitsecond['neutral'].append(neutral)
        predict_per_unitsecond['joy'].append(joy)
        predict_per_unitsecond['love'].append(love)
        predict_per_unitsecond['fear'].append(fear)
        predict_per_unitsecond['surprise'].append(surprise)
        predict_per_unitsecond['sadness'].append(sadness)
        predict_per_unitsecond['anger'].append(anger)
        temp += x
    result = {'predict': predict_per_unitsecond}
    new_predict = Predict7(
        url=url,
        sentiment7_json=result,
    )
    db.add(new_predict)
    db.commit()
    return jsonify(result)
