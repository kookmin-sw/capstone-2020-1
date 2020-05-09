import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest, NotAcceptable

from server.api.Non_url import *
from settings.utils import api
from download.audio import *
from analyze.volume_extract import *
from moviepy.editor import *

app = Blueprint('SNDnormalize', __name__, url_prefix='/api')


@app.route('/SNDnormalize', methods=['GET'])
@api
def get_sound_normalize(data, db):
    req_list = ['url']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest

    url = data['url']

    platform, videoid = extractInfoFromURL(url)

    if platform == "Twitch":
        check = non_url_twitch(videoid)
        isValid = True if check == "recorded" else False
    elif platform == "Youtube":
        check = non_url_youtube(videoid)
        isValid = True if check == "OK" else False
    elif platform == "AfreecaTV":
        check = non_url_afreeca(videoid)
        isValid = True if check > 2 else False

    if isValid == True:
        download(platform, videoid, url)
        audio = AudioFileClip(f"audio/{platform}_{videoid}_NA.mp3")
        volumesPerMinute = sound_extract(platform, videoid)

        audio_arr, avg = local_normalize(audio, volumesPerMinute)

        # arr = audio_arr.to_soundarray()

        return jsonify({"average": avg})
    else:
        raise NotAcceptable # 유효하지 않은 URL
