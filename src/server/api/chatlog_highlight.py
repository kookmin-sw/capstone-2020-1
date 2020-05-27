import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest, NotAcceptable

from models.highlight import ChatHighlight
from settings.utils import api
from download.chatlog import *
from analyze.analysis import *
from api.ana_url import split_url

app = Blueprint('chatlog_highlight', __name__, url_prefix='/api')


@app.route('/chatlog_highlight', methods=['GET'])
@api
def get_chatlog_highlight(data, db):
    req_list = ['url']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest

    url = data['url']

    url_result = split_url(url)

    if url_result != False:
        query = db.query(ChatHighlight).filter(
            ChatHighlight.platform == url_result[0],
            ChatHighlight.videoid == url_result[1],
        ).first()
        if query:
            return jsonify(query.highlight_json)

        log = download(url_result[0], url_result[1])

        point = analyze1_minute(log)

        result = {"highlight": point}

        point = ChatHighlight(
            platform=url_result[0],
            videoid=url_result[1],
            highlight_json=result
        )
        db.add(point)
        db.commit()

        return jsonify(result)
    else:
        raise NotAcceptable  # 유효하지 않은 URL