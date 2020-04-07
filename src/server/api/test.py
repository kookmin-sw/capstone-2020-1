from flask import Blueprint

from settings.utils import api

app = Blueprint('test', __name__, url_prefix='/api')


@app.route('/test', methods=['GET'])
@api
def get_test(data):
    return data


@app.route('/test', methods=['POST'])
@api
def post_test(data):
    return data


@app.route('/test', methods=['PUT'])
@api
def put_test(data):
    return data


@app.route('/test', methods=['DELETE'])
@api
def delete_test(data):
    return data
