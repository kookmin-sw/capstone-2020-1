def test_get_chatlog(client):
    data = {}
    res = client.get('api/analysis_url', query_string=data)
    assert res.status_code == 400
    data['url'] = 'https://www.youtube.com/watch?v=8EVkJqK2gkw'
    res = client.get('api/analysis_url', query_string=data)
    assert res.status_code == 200