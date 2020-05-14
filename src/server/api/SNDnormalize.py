import io
import sys

sys.path.append('../')

from flask import Blueprint, jsonify, request, send_file
from werkzeug.exceptions import BadRequest, NotAcceptable, Conflict, NotFound

from models.file import File

from settings.utils import api
from download.audio import *
from analyze.volume_extract import *

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


def download_image(data, db):
    file = db.query(File).filter(
        File.url == data['url']
    ).first()
    return file


@app.route('/SNDnormalize', methods=['GET'])
@api
def get_sound_normalize(data, db):
    req_list = ['url']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest

    url = data['url']

    file = download_image(data, db)
    if file:  # 해당 url로 저장된 파일 없음
        return send_file(io.BytesIO(file.file),
                         attachment_filename=file.name,
                         as_attachment=True,
                         mimetype='image/png',
                         )

    platform, videoid = extractInfoFromURL(url)

    if platform == "Twitch":
        isValid = non_url_twitch(videoid)
    elif platform == "Youtube":
        isValid = non_url_youtube(videoid)
    elif platform == "AfreecaTV":
        isValid = non_url_afreeca(videoid)

    if isValid:
        download(platform, videoid, url)

        volumesPerMinute = sound_extract(platform, videoid)
        avg = local_normalize(platform, videoid, volumesPerMinute)

        image = {'url': url, 'name': f"./audio/normalizeAudio/{platform}_{videoid}.png"}

        file = open(image['name'], 'rb')
        img = file.read()
        file.close()

        upload_image(image, db)
        return send_file(io.BytesIO(img),
                         attachment_filename=image['name'],
                         as_attachment=True,
                         mimetype='image/png',
                         )

        # return jsonify({"average": avg})
    else:
        raise NotAcceptable  # 유효하지 않은 URL
