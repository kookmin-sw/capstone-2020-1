import io

from flask import Blueprint, jsonify, request, send_file
from models.file import File

from settings.utils import api

app = Blueprint('file', __name__, url_prefix='/api')


@app.route('/upload_wav', methods=['POST'])
@api
def post_test3(data, db):
    new_file = File(
        name=data['name'],
        file=request.files['file'].read(),
        url=data['url'],
    )
    db.add(new_file)
    db.commit()
    return jsonify({'asd': 'qwe'})


@app.route('/download_wav', methods=['GET'])
@api
def get_test3(data, db):
    file = db.query(File).filter(
        File.url == data['url']
    ).first()
    db.commit()
    return send_file(io.BytesIO(file.file),
                     attachment_filename='test_sample.mp3',
                     as_attachment=True,
                     mimetype='audio/wav',
                     )
