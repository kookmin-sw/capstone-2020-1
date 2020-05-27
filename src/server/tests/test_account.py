def test_post_signup(client):  # 회원가입 테스트
    data = {
        'email': 'gjb262@gmail.com',
        'pw': 'yeonsoo2628',
        'name': '김연수',
    }  # 잘못된 회원 정보 생성
    res = client.post('/api/signup', data=data)
    assert res.status_code == 400

    data['age'] = 25  # 필수 회원정보 전부 입력
    res = client.post('/api/signup', data=data)
    assert res.status_code == 200

    res = client.post('/api/signup', data=data)  # 회원가입 중복검사 테스트
    assert res.status_code == 409
