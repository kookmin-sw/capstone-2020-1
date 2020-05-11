import pytest
from flask import json


def test_post_login(client):  # 로그인 테스트
    data = {
        'email': 'gjb262@gmail.com',
    }  # 잘못된 로그인 정보 생성
    res = client.post('api/login', data=data)
    assert res.status_code == 400

    data['pw'] = 'yeonsoo'  # 잘못된 로그인 정보 생성(비밀번호 오류)
    res = client.post('api/login', data=data)
    assert res.status_code == 404

    data['pw'] = 'yeonsoo2628'
    res = client.post('api/login', data=data)
    assert res.status_code == 200

    res_data = json.loads(res.data)
    pytest.uuid = res_data['uuid']  # 로그인 세션 uuid 저장


def test_get_login(client):  # 로그인 만료 테스트
    data = {
        'email': 'gjb262@gmail.com',
    }  # 잘못된 로그인 정보 생성
    res = client.get('api/login', query_string=data)
    assert res.status_code == 400

    data['uuid'] = '41df3f53-d90d-46dc-b127-2069a43989f3'  # 잘못된 uuid 입력
    res = client.get('api/login', query_string=data)
    assert res.status_code == 404

    data['uuid'] = pytest.uuid  # 올바른 유효기간 입력
    res = client.get('api/login', query_string=data)
    assert res.status_code == 200
    assert json.loads(res.data)['uuid'] != data['uuid']  # 새로운 uuid 발급 확인
