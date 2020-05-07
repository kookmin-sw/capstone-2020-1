def test_post_upload_file(client):
    data = {
        'url': 'http://www.sample.sample',
    }  # 잘못된 데이터 생성
    res = client.post('api/upload_wav', data=data, content_type='multipart/form-data')
    assert res.status_code == 400

    data['name'] = 'sample.mp3'  # 파일이 담기지 않은 데이터
    res = client.post('api/upload_wav', data=data, content_type='multipart/form-data')
    assert res.status_code == 400

    with open('tests/sample.mp3', mode='rb') as file:
        data['file'] = file
        res = client.post('api/upload_wav', data=data, content_type='multipart/form-data')
        assert res.status_code == 200

    with open('tests/sample.mp3', mode='rb') as file:
        data['file'] = file
        res = client.post('api/upload_wav', data=data, content_type='multipart/form-data')
        assert res.status_code == 409  # 이미 존재하는 url


def test_get_download_file(client):
    data = {}  # 잘못된 데이터 생성
    res = client.get('api/download_wav', query_string=data)
    assert res.status_code == 400

    data['url'] = 'http://not.exist.url'
    res = client.get('api/download_wav', query_string=data)
    assert res.status_code == 404

    data['url'] = 'http://www.sample.sample'
    res = client.get('api/download_wav', query_string=data)
    assert res.status_code == 200
