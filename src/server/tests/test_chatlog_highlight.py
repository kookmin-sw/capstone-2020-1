def test_get_chatlog_highlight(client):
    data = {
        'videoid': '53773494'
    }
    res = client.get('api/chatlog_highlight', query_string=data)
    assert res.status_code == 400

    data['platform'] = 'AfreecaTV'
    res = client.get('api/chatlog_highlight', query_string=data)
    assert res.status_code == 200
