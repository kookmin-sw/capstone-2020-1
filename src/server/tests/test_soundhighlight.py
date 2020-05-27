from flask import json


def test_get_sound_highlight(client):
    data = {}
    res = client.get('/api/SNDhighlight', query_string=data)
    assert res.status_code == 400

    data = {"url": "http://vod.afreecatv.com/PLAYER/STATION/56750207"}
    res = client.get('/api/SNDhighlight', query_string=data)
    assert res.status_code == 200

    data = {"url": "https://www.twitch.tv/videos/562644795"}  # 유효하지 않은 url
    res = client.get('/api/SNDhighlight', query_string=data)
    assert res.status_code == 406
