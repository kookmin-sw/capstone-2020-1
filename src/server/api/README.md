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
### Find the top 10 keywords
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
    "keyword": [["keyword1", keyword1_freq, [[start_time1, end_time1], ... , [stat_timeN, end_timeN]]], 
                ["keyword2", keyword2_freq, [[start_time1, end_time1], ... , [stat_timeM, end_timeM]]],
                ...
                ["keyword10", keyword10_freq, [[start_time1, end_time1], ... , [stat_timeK, end_timeK]]]]
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
{
    "url": "http://www.sample.sample"
}
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
400 INVALID URL
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
