import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from settings.utils import api
from download.chatlog import *
from analyze.analysis import *
from werkzeug.exceptions import BadRequest

app = Blueprint('chatlog_highlight', __name__, url_prefix='/api')


@app.route('/chatlog_highlight', methods=['GET'])
@api
def get_chatlog_highlight(data, db):
    req_list = ['platform', 'videoid']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest
    platform = data['platform']
    videoid = data['videoid']
    log = download(platform, videoid)

    point = analyze1_minute(log)

    return jsonify({'highlight': point})
