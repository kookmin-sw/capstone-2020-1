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

    data = {"url": "https://www.twitch.tv/videos/562644795"}  # 유효하지 않은 url
    res = client.get('/api/SNDnormalize', query_string=data)
    assert res.status_code == 406
