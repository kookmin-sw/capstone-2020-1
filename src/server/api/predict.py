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

app = Blueprint('predict', __name__, url_prefix='/api')


@app.route('/predict', methods=['GET'])
@api
def get_predict(data, db):
    url = data['url']
    isURLValid = split_url(url)
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
    predict = predict_pos_neg(comment)
    if endSecond >= 100:
        x = math.ceil(endSecond / 100)
    else:
        x = 1
    temp = 0
    predict_per_unitsecond = {'pos': [], 'neg': []}
    while temp < endSecond:
        poscnt = 0
        negcnt = 0
        for i in predict[temp:temp + x]:
            if i == 1:
                poscnt += 1
            else:
                negcnt += 1
        predict_per_unitsecond['pos'].append(poscnt)
        predict_per_unitsecond['neg'].append(negcnt)
        temp += x
    result = {'predict': predict_per_unitsecond}
    new_predict = Predict(
        url=url,
        posneg_json=result,
    )
    db.add(new_predict)
    db.commit()
    return jsonify(result)
