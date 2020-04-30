from flask import json


def test_get_test(client):
    data = {"platform":"Twitch"}
    res = client.get('/api/SNDnormalize', query_string=data)
    assert res.status_code == 400

    data = {"platform":"Twitch", "videoid":562644795,"url":"https://www.twitch.tv/videos/562644795https://www.twitch.tv/videos/562644795"}
    res = client.get('/api/SNDnormalize', query_string=data)
    assert res.status_code == 200