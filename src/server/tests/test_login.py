def test_post_login(client):  # 회원가입 테스트
    data = {
        'email': 'gjb262@gmail.com',
        'pw': 'yeonsoo2628',
        'name': '김연수',
    }  # 잘못된 회원 정보 생성
    res = client.post('/api/login', data=data)
    assert res.status_code == 400

    data['age'] = 25  # 필수 회원정보 전부 입력
    res = client.post('/api/login', data=data)
    assert res.status_code == 200

    res = client.post('/api/login', data=data)  # 회원가입 중복검사 테스트
    assert res.status_code == 409


def test_get_login(client):  # 로그인 테스트
    data = {
        'email': 'gjb262@gmail.com',
    }  # 잘못된 로그인 정보 생성
    res = client.get('api/login', query_string=data)
    assert res.status_code == 400

    data['pw'] = 'yeonsoo'  # 잘못된 로그인 정보 생성(비밀번호 오류)
    res = client.get('api/login', query_string=data)
    assert res.status_code == 404

    data['pw'] = 'yeonsoo2628'
    res = client.get('api/login', query_string=data)
    assert res.status_code == 200
