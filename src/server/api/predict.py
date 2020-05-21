import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from settings.utils import api
from chatsentiment.pos_neg_spm import predict_pos_neg
from werkzeug.exceptions import BadRequest
from api.ana_url import split_url
from download.chatlog import download
import math
from models.highlight import Predict
import numpy
app = Blueprint('predict', __name__, url_prefix='/api')


@app.route('/predict', methods=['GET'])
@api
def get_predict(data, db):
    url = data['url']
    print(1)
    isURLValid = split_url(url)
    print(2)
    if not isURLValid:
        raise BadRequest
    query = db.query(Predict).filter(
        Predict.url == url,
    ).first()
    if query:
        return query.posneg_json
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
    print(3)
    predict = [[s[1:-1] for s in second], predict_pos_neg(comment)]
    print(4)
    if endSecond >= 100.0:
        inc = math.floor(endSecond / 100.0)
    else:
        inc = 1.0
    predict_per_unitsecond = {'pos': [], 'neg': []}
    poscnt = 0; negcnt = 0
    x=inc
    for p in predict:
        if int(p[0]) > x:
            x+=inc
            predict_per_unitsecond['pos'].append(poscnt)
            predict_per_unitsecond['neg'].append(negcnt)
            poscnt=0
        if p[1] == 1:
            poscnt += 1
        elif p[1] == 0:
            negcnt += 1
    print(5)
            

    result = {'predict': predict_per_unitsecond}
    new_predict = Predict(
        url=url,
        posneg_json=result,
    )
    db.add(new_predict)
    db.commit()
    print(6)
    return jsonify(result)
