from flask import Blueprint

app = Blueprint('server', __name__, url_prefix='/api')


@app.route('/ping', methods=['GET'])
def ping():  # 서버 연결 테스트용
    return 'ping'
