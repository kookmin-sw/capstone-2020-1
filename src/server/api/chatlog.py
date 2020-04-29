import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from settings.utils import api
from download.chatlog import *
from analyze.analysis import *

app = Blueprint('chatlog', __name__, url_prefix='/api')


@app.route('/chatlog', methods=['GET'])
@api
def get_chatlog(data, DB):
    platform = data["platform"]
    videoid = data["videoid"]
    log = download(platform, videoid)

    keyword = find_high_frequency_words(log)

    return jsonify({"keyword": keyword})
