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

    url_code = []

    # afree, twitch, youtu에서 오타나는 경우를 생각해서 수정필요

    if "afree" in url:
        if "afreecatv" in url:
            url = re.search(r"http://vod.afreecatv.com/PLAYER/STATION/[0-9]+", url).group()
        videoID = url.split('/')
        videoID = videoID[-1]

        # videoID길이가 8이 아니면 invalid
        if len(videoID) == 8:
            # 오류시 길이 2, 오류 안나면 2초과
            if Non_url.non_url_afreeca(videoID) > 2:
                platform = 'afreecatv'
                url_code = [platform, videoID]
            else:
                return False
        else:
            return False

    elif "twitch" in url:
        url = re.search(r"https://www.twitch.tv/videos/[0-9]+", url).group()
        videoID = url.split('/')
        videoID = videoID[-1]

        # videoID길이가 9가 아니면 invalid
        if len(videoID) == 9:
            # 없는 영상이면 http 에러코드, 아니면 recorded
            if Non_url.non_url_twitch(videoID) != 'recorded':
                return False
            else:
                platform = 'twitch'
                url_code = [platform, videoID]
        else:
            return False

    elif "youtu" in url:
        if 'youtube' in url:
            url = re.search(r"https://www.youtube.com/watch\?v=[a-zA-Z0-_-]+", url).group()
            videoID = url.split('=')
        else:
            url = re.search(r"https://youtu.be/[a-zA-Z0-_-]+", url).group()
            videoID = url.split('/')
        videoID = videoID[-1]

        # videoID길이가 11이 아니면 invalid
        if len(videoID) == 11:
            # 오류나면 Error, 아니면 OK
            if Non_url.non_url_youtube(videoID) == 'OK':
                platform = 'Youtube'
                url_code = [platform, videoID]
            else:
                return False
        else:
            return False

    else:
        return False

    return url_code

def main():
    url = input("url입력:")
    result = split_url(url)
    return result