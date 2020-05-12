import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from settings.utils import api
from chatsentiment.pos_neg_spm import predict_pos_neg
from werkzeug.exceptions import BadRequest
from api.ana_url import split_url
from download.chatlog import download
import math

app = Blueprint('predict', __name__, url_prefix='/api')


@app.route('/predict', methods=['GET'])
@api
def get_predict(data):
    url = data['url']
    platform, videoID = split_url(url)
    download(platform, videoID)
    with open('../../download/chatlog/{}_{}.txt'.format(platform, videoID)) as f:
        content = f.read().split('\n')
    second = []
    content = []
    for i in content:
        splited_chat = i.split('\t')
        second.append(splited_chat[0])
        content.append(splited_chat[2])

    if len(second) < 1 or len(content) < 1:
        raise BadRequest

    endSecond = int(second[-1][1:-1])
    predict = predict_pos_neg(content)
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
    return jsonify({'predict': predict_per_unitsecond})
