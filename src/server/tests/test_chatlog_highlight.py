def test_get_chatlog_highlight(client):
    data = {}
    res = client.get('api/chatlog_highlight', query_string=data)
    assert res.status_code == 400

    data = {"url": "http://vod.afreecatv.com/PLAYER/STATION/96825198"} # 유효하지 않은 url
    res = client.get('api/chatlog_highlight', query_string=data)
    assert res.status_code == 406