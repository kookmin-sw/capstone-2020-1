from flask import json


def test_get_test(client):
    data = dict()
    data['method'] = 'get'
    res = client.get('/api/test', query_string=data)
    assert json.loads(res.data.decode()) == data
    assert res.status_code == 200


def test_post_test(client):
    data = dict()
    data['method'] = 'post'
    res = client.post('/api/test', data=data)
    assert json.loads(res.data.decode()) == data
    assert res.status_code == 200


def test_put_test(client):
    data = dict()
    data['method'] = 'put'
    res = client.put('/api/test', data=data)
    assert json.loads(res.data.decode()) == data
    assert res.status_code == 200


def test_delete_test(client):
    data = dict()
    data['method'] = 'delete'
    res = client.delete('/api/test', query_string=data)
    assert json.loads(res.data.decode()) == data
    assert res.status_code == 200
