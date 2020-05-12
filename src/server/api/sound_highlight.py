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

    """
    if platform == "Twitch":
        check = non_url_twitch(videoid)
        isValid = True if check == "recorded" else False
    elif platform == "Youtube":
        check = non_url_youtube(videoid)
        isValid = False if (check == False) else True
    elif platform == "AfreecaTV":
        check = non_url_afreeca(videoid)
        isValid = False if (check == False) else True
    """
    isValid = True

    if isValid == True:
        download(platform, videoid, url)

        volumesPerMinute = sound_extract(platform, videoid)
        point = analyze1_sound(volumesPerMinute)

        return jsonify({"highlight": point})
    else:
        raise NotAcceptable # 유효하지 않은 URL
