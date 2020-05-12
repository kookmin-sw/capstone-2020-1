from flask import json


def test_get_soundhighlight(client):
    data = {}
    res = client.get('/api/SNDhighlight', query_string=data)
    assert res.status_code == 400

    data = {"url": "https://youtu.be/rOFRZ-zBAbs"}
    res = client.get('/api/SNDhighlight', query_string=data)
    assert res.status_code == 200

    data = {"url": "https://www.twitch.tv/videos/562644795"}  # 유효하지 않은 url
    res = client.get('/api/SNDhighlight', query_string=data)
    assert res.status_code == 406