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
