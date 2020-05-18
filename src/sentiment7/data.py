import sys
sys.path.append('../')
sys.path.append('./')
import os
from download.chatlog import download
from api.ana_url import split_url
import random

def dataGathering():
    URLs = [
        'http://vod.afreecatv.com/PLAYER/STATION/54467101', # 송대익
        'https://youtu.be/VUzT3OEPtQk', # 대도서관
        'http://vod.afreecatv.com/PLAYER/STATION/53773494', # 킹기훈
        'https://www.twitch.tv/videos/570864799', # 진자림
        'http://vod.afreecatv.com/PLAYER/STATION/53719005', # 릴카
        'https://www.twitch.tv/videos/570562539', # 미라지
        'https://www.twitch.tv/videos/568292071', # 짬타수아
        'https://www.youtube.com/watch?v=UF3kcdMqF5w', # 윰댕
        'https://www.youtube.com/watch?v=xn8iDT7wOM0', # 호잇
        'http://vod.afreecatv.com/PLAYER/STATION/53285247' # 에어비스
    ]
    extracted = []
    for url in URLs:
        platform, videoID = split_url(url)
        with open('./chatlog/{}_{}.txt'.format(platform, videoID), encoding='utf-8') as f:
            content = f.readlines()
        nonce = random.randint(0,len(content)-1)
        for i in range(600):
            while content[nonce] in extracted:
                nonce = random.randint(0,len(content)-1)
            extracted.append(content[nonce])
    with open('C:/Users/SJ/Desktop/형준.txt', 'w', encoding='utf-8') as f:
        for i in extracted[:2000]:
            f.write(i)
    with open('C:/Users/SJ/Desktop/정연.txt', 'w', encoding='utf-8') as f:
        for i in extracted[2000:4000]:
            f.write(i)
    with open('C:/Users/SJ/Desktop/진선.txt', 'w', encoding='utf-8') as f:
        for i in extracted[4000:]:
            f.write(i)

def switch(x):
    return {
        '0': 'joy',
        '1': 'love',
        '2': 'sadness',
        '3': 'surprise',
        '4': 'anger',
        '5': 'fear',
        '6': 'neutral',
        'Q': 'Q',
        'q': 'Q'
    }.get(x, False)

def dataLabeling(path, filename):
    idx=0
    with open("{}/{}.txt".format(path, filename), 'r', encoding='utf-8') as origin:
        lines = origin.readlines()
        for line in lines:
            chat = line.split('\t')[2]
            if len(chat) < 1:
                continue
            chat.replace('\n', '\t')
            flag = True
            while flag:
                print("채팅 내용: ", chat, end='')
                num = input("즐거움(0) 사랑(1) 슬픔(2) 놀람(3) 화남(4) 공포(5) 중립(6) // 종료(Q)\n")
                sentiment = switch(num)
                if sentiment != False:
                    flag = False
                    print()
                    break
                print("!!WRONG INPUT!!", end='\n')
                print()
            if sentiment == 'Q':
                break
            rst = sentiment +'\t'+chat
            with open("{}/{}_label.txt".format(path, filename), 'a', encoding='utf-8') as label:
                    label.write(rst)
                    idx+=1
    with open("{}/{}.txt".format(path, filename), 'w', encoding='utf-8') as origin:
        origin.writelines((lines[idx:]))

if __name__ == '__main__':
    path = 'C:/Users/SJ/Desktop'
    filename ='형준'
    # dataGathering()
    dataLabeling(path,filename)