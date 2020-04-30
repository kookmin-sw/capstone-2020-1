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
    
    req_list = ['platform', 'videoid','url']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest

    platform = data['platform']
    videoid = data['videoid']
    url = data['url']
    #url = re.search(r"https://www.twitch.tv/videos/[0-9]+", url).group()
    #videoID = url.split('/')
    #videoID = videoID[-1]
    
    download(platform, videoid, url)
    audio = AudioFileClip(f"audio/{platform}_{videoid}_NA.mp3")
    volumesPerMinute = sound_extract(platform,videoid)
    
    audio_arr, avg = local_normalize(audio, volumesPerMinute)
    #print("1")
    #arr = audio_arr.to_soundarray()
    #print("2")
    
    return jsonify({"average":avg})
