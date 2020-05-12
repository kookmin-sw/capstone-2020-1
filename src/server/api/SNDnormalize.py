import sys

sys.path.append('../')

from flask import Blueprint, jsonify, request, send_file
from werkzeug.exceptions import BadRequest, NotAcceptable, Conflict

from models.file import File

from server.api.Non_url import *
from settings.utils import api
from download.audio import *
from analyze.volume_extract import *
from moviepy.editor import *

app = Blueprint('SNDnormalize', __name__, url_prefix='/api')


def upload_image(data, db):
    query = db.query(File).filter(
        File.url == data['url'],
        File.name == data['name'],
    ).first()
    if query:  # 이미 존재하는 데이터
        raise Conflict

    file = open(data['name'], 'rb')
    img = file.read()
    file.close()

    new_file = File(
        name=data['name'],
        file=img,
        url=data['url'],
    )
    db.add(new_file)
    db.commit()


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
        isValid = non_url_twitch(videoid)
    elif platform == "Youtube":
        isValid = non_url_youtube(videoid)
    elif platform == "AfreecaTV":
        isValid = non_url_afreeca(videoid)

    if isValid == True:
        download(platform, videoid, url)

        volumesPerMinute = sound_extract(platform, videoid)
        avg = local_normalize(platform, videoid, volumesPerMinute)

        image = {'url': url, 'name': f"./audio/normalizeAudio/{platform}_{videoid}.png"}
        upload_image(image, db)

        return jsonify({"average": avg})
    else:
        raise NotAcceptable  # 유효하지 않은 URL
