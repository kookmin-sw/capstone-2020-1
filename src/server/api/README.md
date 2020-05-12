# API 사용법
## 13.209.112.92:8000
### ping 
[GET] /api/ping  
서버 ping 확인용  

요청
```
없음
```
응답
```
ping
```

### test
[GET, POST, PUT, DELETE] /api/test  
데이터 잘 보내고 있는지 확인용

요청
```
{
    자유: 자유
}
```
응답
```
{
    자유: 자유
}
200 ok
```
### signup
[POST] /api/signup  
회원가입

요청
```
{
    "email": "~~@~~.~~"
    "pw": "qwer1234"
    "name": "홍길동"
    "age": 25
}
200 ok
400 요청 형식이 맞지 않음
409 이미 존재하는 계정
```
### login
[GET] /api/login  
로그인 만료여부 조회

요청
```
{
    "email": "~~@~~.~~"
    "uuid": "~~~~-~~~~-~~~~-~~~~"
}
```
응답
```
{
    "email": "~~@~~.~~"
    "expiry": "Sun, 03 May 2020 18:13:18 GMT",
    "uuid": "~~~~-~~~~-~~~~-~~~~"
}
200 ok
400 요청 형식이 맞지 않음
401 이미 만료돼서 재로그인 필요
404 검색 결과가 존재하지 않음
```
[POST] /api/login  
로그인

요청
```
{
    "email": "~~@~~.~~"
    "pw": "qwer1234"
    
}
```
응답
```
{
    "email": "~~@~~.~~"
    "expiry": "Sun, 03 May 2020 18:13:18 GMT",
    "uuid": "~~~~-~~~~-~~~~-~~~~"
}
200 ok
400 요청 형식이 맞지 않음
404 email or pw 오류. 검색결과가 존재하지 않음.
```
### sound normalize
[GET] /api/SNDnormalize
소리 평준화 요청

요청
```
{
    "url": "https://www.youtube.com/watch?v=91crnvnV8f4"
}
```
응답
```
{
    "average":~.~~~
    platform_videoID.png (audio/normalizeAudio 폴더에 생성 및 db에 저장)
}
200 ok
400 요청 형식이 맞지 않음
406 유효하지 않은 URL
409 이미 들어왔던 데이터
```
### The top 10 keywords
[GET] /api/chatlog  
상위 10개 키워드와 출연구간 추출 요청

요청
```
{
    "platform": "AfreecaTV",
    "videoid": "53773494"
}
```
응답
```
{
    "keyword": [['기훈', 276, [[3206, 3249]]], 
                ['얼음', 269, [[2597, 2720], [2734, 2794], [2872, 2982], [3078, 3127], [3172, 3199], [3614, 3645]]], 
                ['돼지', 145, [[1696, 1712], [2891, 2920], [2990, 3018], [3361, 3377]]], 
                ['우유', 118, [[2577, 2624], [3673, 3697]]], 
                ['그냥', 98, [[3141, 3173]]], 
                ['유하', 74, [[750, 785], [835, 874]]], 
                ['김정은', 63, [[1698, 1709], [2891, 2911], [3354, 3381]]], 
                ['숟가락', 47, [[3480, 3546]]], 
                ['식사', 42, [[2980, 2999]]], 
                ['설탕', 39, [[1346, 1404]]]] 
                (키워드, 출현 빈도수, [[출현 구간1(start), 출현 구간1(end)], ... , [출현 구간n(start), 출현 구간n(end)])
    AfreecaTV_53773494.txt (chatlog 폴더에 생성)
}
200 ok
400 요청 형식이 맞지 않음
```
### URL Validation
[GET] /api/analysis_url
영상정보를 얻어올 수 있는 URL인지 확인

요청
```
{
    "url" : "https://www.youtube.com/watch?v=N73yXoFzcLk"
}
```
응답
```
{
    "Platfrom, VideoID " : ['Youtube', 'N73yXoFzcLk']
}
200 ok
400 요청 형식이 맞지 않음
```
### file upload and download
[POST] api/upload_file  
데이터베이스에 파일 업로드(form-data)

요청
```
{
    "name": "sample.mp3"
    "url": "http://www.sample.sample"(영상 url)
    "file": sample.mp3
}
```
응답
```
{
    "result": "success"
}
200 ok
400 요청 형식이 맞지 않음
409 이미 존재하는 url
```
[GET] /api/download_file  
오디오파일 다운로드

요청
```
{
    "url": "http://www.sample.sample"
}
```
응답
```
{
    file 
}
200 ok
400 요청 형식이 맞지 않음
404 해당 url과 연관된 파일이 없음
```

### Predict
채팅 긍정부정 분류

요청
```
Query string: second=[1]&second=[2]&second=[3]&content=content1&content=content2&content=content3
```
응답
```
{
  "predict": {
    "neg": [
      1, 
      1, 
      0
    ], 
    "pos": [
      0, 
      0, 
      1
    ]
  }
}
200 OK
400 요청 형식이 맞지 않음
```
### sound highlight
[GET] /api/SNDhighlight
소리 하이라이트 지점 추출

요청
```
{
    "url": "https://www.youtube.com/watch?v=91crnvnV8f4"
}
```
응답
```
{
    "highlight": [ [7, 0.22350525808284777], [26, 0.3252495816137475], [53, 0.21840620858731044] ] (하이라이트 지점(분), 해당 지점의 소리 크기)
}
200 ok
400 요청 형식이 맞지 않음
406 유효하지 않은 URL
```
### chatlog highlight
[GET] /api/chatlog_highlight  
채팅로그 하이라이트 지점 추출

요청
```
{
    "platform": "AfreecaTV",
    "videoid": "53773494"
}
```
응답
```
{
    "highlight": [ [1702, 12], [2896, 19], [3365, 12] ] (하이라이트 지점(초), 해당 지점의 채팅량)
    AfreecaTV_53773494.txt (chatlog 폴더에 생성)
}
200 ok
400 요청 형식이 맞지 않음
```