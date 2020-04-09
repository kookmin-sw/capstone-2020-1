def test_ping(client):
    res = client.get('api/ping')
    assert res.data.decode() == 'ping'  # ping 텍스트 확인
    assert res.status_code == 200
