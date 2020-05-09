import sys

sys.path.append('../')

from flask import Blueprint, jsonify
from settings.utils import api
from download.audio import *
from analyze.volume_extract import *
from moviepy.editor import *
from werkzeug.exceptions import BadRequest

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
    download(platform, videoid, url)
    audio = AudioFileClip(f"audio/{platform}_{videoid}_NA.mp3")
    volumesPerMinute = sound_extract(platform, videoid)

    audio_arr, avg = local_normalize(audio, volumesPerMinute)
    # arr = audio_arr.to_soundarray()

    return jsonify({"average": avg})
