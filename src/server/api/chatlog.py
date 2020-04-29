import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from settings.utils import api
from download.chatlog import *
from analyze.analysis import *
from werkzeug.exceptions import BadRequest

app = Blueprint('chatlog', __name__, url_prefix='/api')


@app.route('/chatlog', methods=['GET'])
@api
def get_chatlog(data, db):
    req_list = ['platform', 'videoid']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest
    platform = data['platform']
    videoid = data['videoid']
    log = download(platform, videoid)

    keyword = find_high_frequency_words(log)

    return jsonify({'keyword': keyword})
