import json
import os
import re
import requests
import youtube_dl
from ast import literal_eval
from bs4 import BeautifulSoup


# pip3 install youtube-dl


def download(platform, videoID, url):
    dw_opts = {'format': 'worstaudio/worst', 'extractaudio': True, 'audioformat': "mp3",
               'outtmpl': "audio/" + platform + '_' + videoID + '_' + '%(playlist_index)s' + ".mp3"}
    try:
        with youtube_dl.YoutubeDL(dw_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print('error', e)
    print('Finish!')


def extractInfoFromURL(url):
    if "afree" in url:
        platform = "AfreecaTV"
        if "afreecatv" in url:
            url = re.search(r"http://vod.afreecatv.com/PLAYER/STATION/[0-9]+", url).group()
        videoID = url.split('/')
        videoID = videoID[-1]
    elif "twitch" in url:
        platform = "Twitch"
        url = re.search(r"https://www.twitch.tv/videos/[0-9]+", url).group()
        videoID = url.split('/')
        videoID = videoID[-1]
    elif "youtu" in url:
        platform = "Youtube"
        if 'youtube' in url:
            url = re.search(r"https://www.youtube.com/watch\?v=[a-zA-Z0-9_-]+", url).group()
            videoID = url.split('=')
        else:
            url = re.search(r"https://youtu.be/[a-zA-Z0-9_-]+", url).group()
            videoID = url.split('/')
        videoID = videoID[-1]

    if not os.path.exists("./audio"):
        os.makedirs("./audio")

    return platform, videoID


def non_url_twitch(videoID):
    url = 'https://api.twitch.tv/v5/videos/' + videoID
    client_id = "x7cy2lvfh9aob9oyset31dhbfng1tc"
    param = {"content_offset_seconds": 0}
    response = requests.get(url, params=param, headers={"Client-ID": client_id})
    # 없는 영상이면 http 에러코드, 아니면 recorded
    j = json.loads(response.text)
    return True if j['status'] == "recorded" else False


def non_url_afreeca(videoID):
    url = 'http://vod.afreecatv.com/PLAYER/STATION/' + videoID
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    # 아프리카는 동영상이 없으면 따로 페이지 없이 <script>한줄만 나타남(확인창?)
    # 오류시 길이 2, 오류 안나면 2초과
    len_soup = len(soup)

    return True if len_soup > 2 else False


def non_url_youtube(videoID):
    url = "https://www.youtube.com/watch?v=" + videoID
    print(url)
    dict_str = ""

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")

    # 상태가 담겨있는 script
    for scrp in soup.find_all("script"):
        txt = scrp.text
        if 'ytInitialPlayerResponse' in txt:
            dict_str = scrp.text.split('["ytInitialPlayerResponse"] = ')[1]
            dict_str = dict_str.split('if (window.ytcsi)')[0]
            break

    # javascript 표기이므로 변형
    dict_str = dict_str.replace('false', 'False')
    dict_str = dict_str.replace('true', 'True')

    # 불필요한 공백 등 제거
    dict_str = dict_str.rstrip(' \n;()')

    # 사전 형식으로 변환
    dics = literal_eval(dict_str)
    new_dics = dics["playabilityStatus"]["status"]

    # 오류나면 Error, 아니면 OK
    return True if new_dics == "OK" else False
