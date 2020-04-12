import requests
import json
from bs4 import BeautifulSoup
from requests.compat import urlparse
from xml.etree import ElementTree
from ast import literal_eval
import math
import os
import matplotlib.pyplot as plt
import re


def visualization(chatlist):
    plt.bar(range(len(chatlist)), chatlist)
    plt.show()


def count_chat_each_second(flatform, videoID):
    filename = "./chatlog/"+flatform+"_"+videoID+".txt"
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
        chats=[0 for _ in range(int(data[-1].split(' ')[0][1:-1])+1)]
        for i in data:
            temp = i.split(' ')[0]
            second = temp[1:len(temp)-1]
            chats[int(second)] +=1
    return chats


def array_to_file(platform, arr, filename): # 배열을 텍스트 파일로 저장하는 함수
    if not os.path.exists("./chatlog"):
        os.makedirs("./chatlog")
    data = "./chatlog/"+platform + "_" + filename + ".txt"
    with open(data, 'w', encoding="utf-8") as f:
        for x in range(0, len(arr)):
            if arr[x][0] == "0": continue
            f.write('[')
            f.write(str(arr[x][0]))
            f.write(']')
            f.write(' ')
            f.write('(')
            f.write(str(arr[x][1]))
            f.write(')')
            f.write(' ')
            f.write(str(arr[x][2].replace('\n', '')))
            f.write("\n")
    f.close()


def afreeca(platform, videoID): # 아프리카 채팅기록을 튜플로 추출하는 함수
    data = []
    url = "http://vod.afreecatv.com/PLAYER/STATION/" + videoID
    info_url = "http://afbbs.afreecatv.com:8080/api/video/get_video_info.php?"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"

    # StationNo(방송국 ID, 방송국에 여러 BJ 소속가능)와 nBbsNo(게시판 ID, 방송국 홈피에 여러 게시판 존재) 찾기
    html = requests.get(url, params=None, headers={'user-agent': user_agent})
    dom = BeautifulSoup(html.text, 'lxml')

    metatag = dom.select_one("meta[property='og:video']")['content']
    station_id = re.search(r"nStationNo=[0-9]+", metatag).group()
    station_id = station_id[11:]
    bbs_id = re.search(r"nBbsNo=[0-9]+", metatag).group()
    bbs_id = bbs_id[7:]
    info_url += ("nTitleNo=" + str(videoID) + "&nStationNo=" + str(station_id) + "&nBbsNo=" + str(bbs_id))

    # rowKey 찾기(동영상 하나에 1개 이상 존재)
    xml = requests.get(info_url, params=None, headers={'user-agent': user_agent})
    root = ElementTree.fromstring(xml.text)

    rowKey_list = []
    duration_list = [0]
    for file in root.iter('file'):
        if file.attrib.get('key') is not None:
            rowKey_list.append(file.attrib.get('key'))
            duration_list.append(int(file.attrib.get('duration')) + duration_list[-1])

    # 채팅 로그 추출하기
    url = "http://videoimg.afreecatv.com/php/ChatLoad.php"
    for idx, rowKey in enumerate(rowKey_list):
        i = 0
        while True:
            key = "rowKey=" + rowKey + "_c&startTime=" + str(3600 * i)
            xml = requests.get(url, params=key, headers={'user-agent': user_agent})
            try:
                xmltree = ElementTree.XML(xml.text)
            except ElementTree.ParseError:  # 더 이상의 채팅기록이 없어 에러가 발생하면 break
                break
            data.extend(zip(map(lambda x: math.trunc(float(x.text)) + duration_list[idx], xmltree.findall('chat/t')),
                            map(lambda x: x.text, xmltree.findall('chat/u')),
                            map(lambda x: x.text, xmltree.findall('chat/m'))))
            i += 1
    array_to_file(platform, data, videoID)
    return data


def twitch(platform, videoID): # 트위치 채팅기록을 리스트로 추출하는 함수
    data = []
    url = 'https://api.twitch.tv/v5/videos/' + videoID + '/comments'
    client_id = "x7cy2lvfh9aob9oyset31dhbfng1tc"

    param = {"content_offset_seconds": 0}

    while True:
        # 처음에는 content_offset_seconds 파라미터를 이용
        # 이 후부터는 cursor 파라미터로 다음 받아올 값들을 추적
        response = requests.get(url, params=param, headers={"Client-ID": client_id})

        j = json.loads(response.text)

        for k in range(0, len(j["comments"])):
            time = math.trunc(float(j["comments"][k]["content_offset_seconds"]))
            user = j["comments"][k]["commenter"]["display_name"]
            comment = j["comments"][k]["message"]["body"]
            data.append([time, user, comment])

        if '_next' not in j:
            break

        param = {"cursor": j["_next"]}
    array_to_file(platform, data, videoID)
    return data


def youtube(platform, videoID):
    data = []
    url = "https://www.youtube.com/watch?v=" + videoID

    dict_str = ""
    next_url = ""
    session = requests.Session()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    # 채팅이 담겨있는 iframe
    for frame in soup.find_all("iframe"):
        if ("live_chat_replay" in frame["src"]):
            next_url = frame["src"]
            break

    while (1):
        try:
            xml = session.get(next_url, headers=headers)
            soup = BeautifulSoup(xml.text, 'lxml')

            # next_url의 데이터가 있는 부분을 find_all에서 찾고 split로 쪼갠다
            for scrp in soup.find_all("script"):
                txt = scrp.text
                if 'responseContext' in txt:
                    dict_str = scrp.text.split("] = ")[1]
                    break

            # javascript 표기이므로 변형
            dict_str = dict_str.replace('false', 'False')
            dict_str = dict_str.replace('true', 'True')
            # dict_str = dict_str.replace("'", '-')

            # 불필요한 공백 등 제거
            dict_str = dict_str.rstrip(' \n;()')

            # 사전 형식으로 변환
            dics = literal_eval(dict_str)

            continue_url = \
            dics["continuationContents"]["liveChatContinuation"]["continuations"][0]["liveChatReplayContinuationData"][
                "continuation"]
            next_url = "https://www.youtube.com/live_chat_replay?continuation=" + continue_url

            # 코멘트 데이터의 목록. 선두는 노이즈 데이터이므로 [1 :]에서 저장
            dics2 = dics["continuationContents"]["liveChatContinuation"]["actions"][1:]

            for samp in enumerate(dics2):
                samp = samp[1]
                chat = ""
                chat_id = ""
                de_chat = samp["replayChatItemAction"]["actions"][0]
                de_time = int(int(samp["replayChatItemAction"]["videoOffsetTimeMsec"]) / 1000)
                de_str = str(de_chat)

                if "liveChatPlaceholderItemRenderer" in de_str:
                    continue
                elif "addLiveChatTickerItemAction" in de_str:
                    continue
                elif "liveChatPaidStickerRenderer" in de_str:
                    continue
                elif "liveChatPaidMessageRenderer" in de_str:
                    continue

                else:
                    if "liveChatMembershipItemRenderer" in de_str:
                        continue
                    else:
                        chat_log = de_chat["addChatItemAction"]["item"]["liveChatTextMessageRenderer"]["message"][
                            "runs"]
                        for i in range(len(chat_log)):
                            sample = chat_log[i]
                            if "emoji" in sample:
                                chat = chat
                            else:
                                chat += chat_log[i]["text"]
                        chat_id = de_chat["addChatItemAction"]["item"]["liveChatTextMessageRenderer"]["authorName"][
                            "simpleText"]

                # 리스트에 추출 항목들 저장
                el = [str(de_time), str(chat_id), str(chat)]
                data.append(el)

        # next_url를 사용할 수 없게되면 while문 종료
        except:
            break
    array_to_file(platform, data, videoID)
    return data


def download(platform, videoID):
    if platform == "AfreecaTV":
        return afreeca(platform, videoID)
    elif platform == "Twitch":
        return twitch(platform, videoID)
    elif platform == "Youtube":
        return youtube(platform, videoID)


if __name__ == '__main__':
    url = input("stream url : ")

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

    if not os.path.exists("./chatlog"):
        os.makedirs("./chatlog")
    if platform + '_' + videoID + ".txt" in os.listdir("./chatlog"):
        print('This chatlog file has already been requested.')
    else:
        chat_data = download(platform, videoID)