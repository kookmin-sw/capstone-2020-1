from flask import Blueprint, jsonify
from settings.utils import api
from download.chatlog import *


app = Blueprint('chatlog', __name__, url_prefix='/api')


@app.route('/chatlog', methods=['GET'])
@api

def get_chatlog(data, DB):
    platform = data["platform"]
    videoid = data["videoid"]
    res = download(platform, videoid)

    return jsonify({"result": res})