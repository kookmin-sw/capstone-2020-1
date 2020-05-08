from urllib.parse import urlencode

def test_get_predict(client):
    res = client.get('api/predict', query_string='second=[1]&second=[2]&second=[3]')
    assert res.status_code == 400

    res = client.get('api/predict', query_string='second=[1]&second=[2]&second=[3]&content=개웃경ㅋ&content=재미없다&content=꿀잼ㅋ')
    assert res.status_code == 200
