from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound, BadRequest, Conflict

from api.models.user_info import UserInfo
from settings.serialize import serialize
from settings.utils import api

app = Blueprint('login', __name__, url_prefix='/api')


@app.route('/login', methods=['GET'])
@api
def get_login(data, db):  # 회원정보 불러옴
    req_list = ['email', 'pw']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest
    user_info = db.query(UserInfo).filter(
        UserInfo.email == data['email'],
        UserInfo.pw == data['pw'],
    ).first()
    if not user_info:  # 검색 결과 없음
        raise NotFound
    return jsonify(serialize(user_info))


@app.route('/login', methods=['POST'])
@api
def post_login(data, db):
    req_list = ['email', 'pw', 'name', 'age']
    for i in req_list:  # 필수 요소 들어있는지 검사
        if i not in data:
            raise BadRequest

    user_info = db.query(UserInfo).filter(
        UserInfo.email == data['email'],
        UserInfo.pw == data['pw'],
    ).first()
    if user_info:  # 이미 존재하는 계정
        raise Conflict

    db.add(UserInfo(
        email=data['email'],
        pw=data['pw'],
        name=data['name'],
        age=data['age'],
    ))
    db.commit()

    return jsonify({'signup': 'success'})
