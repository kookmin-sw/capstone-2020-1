import urllib.request
import re
import requests
from bs4 import BeautifulSoup
from . import Non_url

def split_url(url):
    res = urllib.request.urlopen(url)
    # 작동하는 url인지 확인
    if res.status != 200:
        return False

    el = []

    # afree, twitch, youtu에서 오타나는 경우를 생각해서 수정필요

    if "afree" in url:
        if "afreecatv" in url:
            url = re.search(r"http://vod.afreecatv.com/PLAYER/STATION/[0-9]+", url).group()
        videoID = url.split('/')
        videoID = videoID[-1]

        if len(videoID) == 8:
            if Non_url.non_url_afreeca(url) > 2:
                platform = Platform(url)
                el = [platform, videoID]
            else:
                return False
        else:
            return False

    elif "twitch" in url:
        url = re.search(r"https://www.twitch.tv/videos/[0-9]+", url).group()
        videoID = url.split('/')
        videoID = videoID[-1]

        if len(videoID) == 9:
            if Non_url.non_url_twitch(videoID) != 'recorded':
                return False
            else:
                platform = Platform(url)
                el = [platform, videoID]
        else:
            return False

    elif "youtu" in url:
        platform = "Youtube"
        if 'youtube' in url:
            url = re.search(r"https://www.youtube.com/watch\?v=[a-zA-Z0-_-]+", url).group()
            videoID = url.split('=')
        else:
            url = re.search(r"https://youtu.be/[a-zA-Z0-_-]+", url).group()
            videoID = url.split('/')
        videoID = videoID[-1]

        if len(videoID) == 11:
            if Non_url.non_url_youtube(url) == 'OK':
                platform = Platform(url)
                el = [platform, videoID]
            else:
                return False
        else:
            return False

    else:
        return False

    return el

def Platform(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    html = requests.get(url, headers = headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    metatag = soup.find('meta', {'property': 'og:site_name'}).get('content')

    # 입력된 url에서 platform 확인
    metatag = metatag.lower()

    return metatag

#url = input("url입력:")
#t = split_url(url)
#print(t)