from flask import Blueprint
from settings.utils import api
from api.models.user_info import UserInfo

app = Blueprint('login', __name__, url_prefix='/api')


@app.route('/login', methods=['GET'])
@api
def get_login(data):
    return data['get']


@app.route('/login', methods=['POST'])
@api
def post_login(data, db):

    return data['post']
