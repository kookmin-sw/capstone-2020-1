from urllib.parse import urlencode

def test_get_predict(client):
    data = {
        'url': 'asdfawefasdf'
    }
    res = client.get('api/predict', query_string=data)
    assert res.status_code == 400
    data = {
        'url': 'https://www.youtube.com/watch?v=8EVkJqK2gkw'
    }
    res = client.get('api/predict', query_string=data)
    assert res.status_code == 200
