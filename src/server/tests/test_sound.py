from flask import json


def test_get_normalize(client):
    data = {}
    res = client.get('/api/SNDnormalize', query_string=data)
    assert res.status_code == 400

    data = {"url": "http://vod.afreecatv.com/PLAYER/STATION/56750207"}  # 처음 들어오는 데이터
    res = client.get('/api/SNDnormalize', query_string=data)
    assert res.status_code == 200
    assert len(json.loads(res.get_data())['image_url']) > 0

    data = {"url": "https://www.twitch.tv/videos/562644795"}  # 유효하지 않은 url
    res = client.get('/api/SNDnormalize', query_string=data)
    assert res.status_code == 406
