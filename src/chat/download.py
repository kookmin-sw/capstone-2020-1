import requests
from bs4 import BeautifulSoup
from requests.compat import urlparse
from xml.etree import ElementTree

def double_digit(num): # 63.158 → 01:03 형식 변환하는 함수
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)


def array_to_file(arr, filename): # 배열을 텍스트 파일로 저장하는 함수
    with open(filename + ".txt", 'wt', encoding="utf-8") as f:
        for x in range(0, len(arr)):
            second = arr[x][0]
            minute = int(second / 60)
            if minute >= 60:
                hour = int(minute / 60)
                minute %= 60
            else:
                hour = int(minute / 60)
            second = int(second % 60)
            time = double_digit(hour) + ':' + double_digit(minute) + ':' + double_digit(second)

            f.write('(')
            f.write(time)
            f.write(')')
            f.write(' ')
            f.write('[')
            f.write(arr[x][1])
            f.write(']')
            f.write(' ')
            f.write(arr[x][2])
            f.write("\n")
    f.close()


def afreeca(video_id): # 아프리카 채팅기록을 튜플로 추출하는 함수
    url = "http://vod.afreecatv.com/PLAYER/STATION/" + video_id
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"

    html = requests.get(url, params=None, headers={'user-agent': user_agent})
    dom = BeautifulSoup(html.text, 'lxml')
    metatag = dom.select_one("meta[property='og:image']")['content']
    rowKey = urlparse(metatag).query
    rowKey = rowKey[:-1] + "c&startTime="

    i = 0
    data = []
    url = "http://videoimg.afreecatv.com/php/ChatLoad.php"
    while True:
        key = rowKey + str(3600 * i)
        xml = requests.get(url, params=key, headers={'user-agent': user_agent})
        try:
            xmltree = ElementTree.XML(xml.text)
        except ElementTree.ParseError: # 더 이상의 채팅기록이 없어 에러가 발생하면 break
            break
        data.extend(zip(map(lambda x: float(x.text), xmltree.findall('chat/t')), map(lambda x: x.text, xmltree.findall('chat/u')), map(lambda x: x.text, xmltree.findall('chat/m'))))
        i += 1
    #print(data)
    array_to_file(data, video_id)
    return data