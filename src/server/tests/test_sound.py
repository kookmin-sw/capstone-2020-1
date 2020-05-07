from flask import json


def test_get_test(client):
    data = {"platform": "Twitch"}
    res = client.get('/api/SNDnormalize', query_string=data)
    assert res.status_code == 400

    data = {"platform": "youtube",
            "videoid": 0,
            "url": "https://youtu.be/rOFRZ-zBAbs"}
    res = client.get('/api/SNDnormalize', query_string=data)
    assert res.status_code == 200
