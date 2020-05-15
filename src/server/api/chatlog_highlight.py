import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest

from models.highlight import ChatHighlight
from settings.utils import api
from download.chatlog import *
from analyze.analysis import *

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

    result = {'highlight': point}

    point = ChatHighlight(
        platform=platform,
        videoid=videoid,
        highlight_json=result
    )
    db.add(point)
    db.commit()

    return jsonify(result)
