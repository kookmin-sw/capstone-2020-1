import io

from flask import Blueprint, jsonify, request, send_file
from werkzeug.exceptions import BadRequest, Conflict, NotFound

from models.file import File
from settings.utils import api

app = Blueprint('file', __name__, url_prefix='/api')


@app.route('/upload_wav', methods=['POST'])
@api
def post_upload_file(data, db):
    req_list = ['name', 'url']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest
    if 'file' in request.files:  # 파일 존재하는지 검사
        raise BadRequest

    query = db.query(File).filter(
        File.url == data['url']
    ).first()
    if query:  # 이미 존재하는 url
        raise Conflict

    new_file = File(
        name=data['name'],
        file=request.files['file'].read(),
        url=data['url'],
    )
    db.add(new_file)
    db.commit()
    return jsonify({'result': 'success'})


@app.route('/download_wav', methods=['GET'])
@api
def get_download_file(data, db):
    if 'url' not in data:  # 필수 요소 들어있는지 검사
        raise BadRequest

    file = db.query(File).filter(
        File.url == data['url']
    ).first()
    if not file:  # 해당 url로 저장된 파일 없음
        raise NotFound
    return send_file(io.BytesIO(file.file),
                     attachment_filename='test_sample.mp3',
                     as_attachment=True,
                     mimetype='audio/wav',
                     )
