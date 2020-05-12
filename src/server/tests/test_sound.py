from flask import json


def test_get_normalize(client):
    data = {}
    res = client.get('/api/SNDnormalize', query_string=data)
    assert res.status_code == 400

    data = {"url": "https://youtu.be/rOFRZ-zBAbs"} # 처음 들어오는 데이터
    res = client.get('/api/SNDnormalize', query_string=data)
    assert res.status_code == 200

    data = {"url": "https://youtu.be/rOFRZ-zBAbs"} # 이미 들어왔던 데이터
    res = client.get('/api/SNDnormalize', query_string=data)
    assert res.status_code == 409
