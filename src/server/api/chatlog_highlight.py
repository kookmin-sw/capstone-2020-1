import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest, NotAcceptable

from settings.utils import api
from download.chatlog import *
from analyze.analysis import *
from api.ana_url import split_url

app = Blueprint('chatlog_highlight', __name__, url_prefix='/api')


@app.route('/chatlog_highlight', methods=['GET'])
@api
def get_chatlog_highlight(data, db):
     = ['url']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest

    url = data['url']

    url_result = split_url(url)

    if url_result != False:
        log = download(url_result[0], url_result[1])

        point = analyze1_minute(log)
        req_list
        result = {"highlight": point}

        return jsonify(result)
    else:
        raise NotAcceptable  # 유효하지 않은 URL