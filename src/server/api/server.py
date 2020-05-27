import os

from flask import Blueprint, json, Response, request

app = Blueprint('server', __name__, url_prefix='/api')


@app.route('/ping', methods=['GET'])
def ping():  # 서버 연결 테스트용
    return 'ping'


@app.route('/deploy', methods=['POST'])
def hooks():
    res = json.dumps(request.form)
    res = json.loads(res)
    res = json.loads(res['payload'])
    root_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    if res['ref'] == 'refs/heads/deploy':
        os.system(f'sh {root_dir}/settings/hooks.sh')
    return Response('push', status=200)
