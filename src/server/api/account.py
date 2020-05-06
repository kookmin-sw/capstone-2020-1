from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest, Conflict

from api.models.user_info import UserInfo
from settings.serialize import serialize
from settings.utils import api

app = Blueprint('account', __name__, url_prefix='/api')


@app.route('/signup', methods=['POST'])
@api
def post_signup(data, db):
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

    user_info = UserInfo(
        email=data['email'],
        pw=data['pw'],
        name=data['name'],
        age=data['age'],
    )
    db.add(user_info)
    db.commit()

    return jsonify(serialize(user_info))
