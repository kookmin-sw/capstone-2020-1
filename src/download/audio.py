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