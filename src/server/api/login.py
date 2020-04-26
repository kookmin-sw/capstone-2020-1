from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound, BadRequest

from api.models.user_info import UserInfo
from settings.serialize import serialize
from settings.utils import api

app = Blueprint('login', __name__, url_prefix='/api')


@app.route('/login', methods=['GET'])
@api
def get_login(data, db):  # 회원정보 불러옴
    user_info = db.query(UserInfo).filter(
        UserInfo.email == data['email'],
        UserInfo.pw == data['pw'],
    ).first()
    if not user_info:
        raise NotFound
    return jsonify(serialize(user_info))


@app.route('/login', methods=['POST'])
@api
def post_login(data, db):
    req_list = ['email', 'pw', 'name', 'age']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest

    db.add(UserInfo(
        email=data['email'],
        pw=data['pw'],
        name=data['name'],
        age=data['age'],
    ))
    db.commit()

    return 'success'
