import sys

sys.path.append('../')

from flask import Blueprint, jsonify, request
from settings.utils import api
from chatsentiment.pos_neg_spm import *
from werkzeug.exceptions import BadRequest
from urllib.parse import urlencode
import math

app = Blueprint('predict', __name__, url_prefix='/api')


@app.route('/predict', methods=['GET'])
@api
def get_predict(data, db):
    second = request.args.getlist("second")
    content = request.args.getlist("content")
    if len(second) < 1 or len(content) < 1:
        raise BadRequest
    
    print(second)
    print(content)
    endSecond = int(second[-1][1:-1])
    print(endSecond)
    predict = predict_pos_neg(content)
    print(predict)
    if endSecond >= 100:
        x = math.ceil(endSecond/100)
    else:
        x = 1
    temp = 0
    predict_per_unitsecond={'pos': [], 'neg': []}
    while temp < endSecond:
        poscnt=0
        negcnt=0
        for i in predict[temp:temp+x]:
            if i == 1:
                poscnt+=1
            else:
                negcnt+=1
        predict_per_unitsecond['pos'].append(poscnt)
        predict_per_unitsecond['neg'].append(negcnt)
        temp+=x
    return jsonify({'predict': predict_per_unitsecond})
