import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest, NotAcceptable

from server.api.Non_url import *
from settings.utils import api
from download.audio import *
from analyze.volume_extract import *
from analyze.analysis import *

app = Blueprint('SNDhighlight', __name__, url_prefix='/api')


@app.route('/SNDhighlight', methods=['GET'])
@api
def get_sound_normalize(data, db):
    req_list = ['url']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest

    url = data['url']

    platform, videoid = extractInfoFromURL(url)

    if platform == "Twitch":
        isValid = non_url_twitch(videoid)
    elif platform == "Youtube":
        isValid = non_url_youtube(videoid)
    elif platform == "AfreecaTV":
        isValid = non_url_afreeca(videoid)

    if isValid == True:
        download(platform, videoid, url)

        volumesPerMinute = sound_extract(platform, videoid)
        point = analyze1_sound(volumesPerMinute)

        return jsonify({"highlight": point})
    else:
        raise NotAcceptable # 유효하지 않은 URL
