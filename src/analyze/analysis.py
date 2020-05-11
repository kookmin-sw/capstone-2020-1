import numpy as np
import matplotlib.pyplot as plt
from konlpy.tag import Okt
import operator

okt = Okt()

def visualization(chatlist):
    plt.bar(range(len(chatlist)), chatlist)
    plt.show()


def print_point_hhmmss(point):
    for i in range(len(point)):
        seconds = point[i][0]
        hours = seconds // (60 * 60)
        seconds %= (60 * 60)
        minutes = seconds // 60
        seconds %= 60
        print("%02i:%02i:%02i" % (hours, minutes, seconds), point[i][1])


def print_point_hhmm(point):
    for i in range(len(point)):
        minutes = point[i][0]
        hours = minutes // 60
        minutes %= 60
        print("%02i:%02i" % (hours, minutes), point[i][1])


def print_section_hhmmss(section):
    for i in range(len(section)):
        print("{:<3}".format(i+1), end='\t')
        print("{:<15}".format(section[i][0]), end='\t')
        j = 0
        while j < len(section[i][1]):
            seconds = section[i][1][j][0]
            hours = seconds // (60 * 60)
            seconds %= (60 * 60)
            minutes = seconds // 60
            seconds %= 60
            print("%02i:%02i:%02i" % (hours, minutes, seconds), end='-')
            seconds = section[i][1][j][1]
            hours = seconds // (60 * 60)
            seconds %= (60 * 60)
            minutes = seconds // 60
            seconds %= 60
            print("%02i:%02i:%02i" % (hours, minutes, seconds), end='\t')
            j += 2
        print()


def analyze1(data, comment=None):  # 초당 채팅 수 계산
    second = []
    if comment is None:
        # 채팅 기록에서 모든 comment의 시간 추출
        for i in range(len(data)):
            second.append(int(data[i][0]))
    else:
        # 채팅 기록에서 특정 comment가 포함된 채팅 시간 추출
        for i in range(len(data)):
            if comment in data[i][2]:
                second.append(int(data[i][0]))

    count = []
    for i in range(int(data[len(data) - 1][0]) + 1):
        count.append(0)

    for x in second:
        count[x] += 1

    average = np.mean(np.array(count))

    # 오름차순으로 정렬한 후 10 번째로 많은 채팅 수를 구함
    sorted_list = sorted(count)
    max10th = sorted_list[-10]

    point = []
    for i in range(len(count)):
        if count[i] >= max10th:
            point.append((i, count[i]))

    #visualization(count)
    print_point_hhmmss(point)
    return point


def analyze2(data):  # 초당 채팅 참가자 수 계산
    second = []

    for i in range(len(data)):
        second.append(int(data[i][0]))

    count_s = []
    for i in range(int(data[len(data) - 1][0]) + 1):
        count_s.append(0)

    for x in second:
        count_s[x] += 1

    base = 0
    user = []
    count_u = []
    temp = []
    for i in range(len(count_s)):
        x = count_s[i]
        for j in range(base, base + x):
            temp.append(data[j][1])
        temp = list(set(temp))
        count_u.append(len(temp))
        user.extend(temp)
        user = list(set(user))
        base += x
        temp = []
    #total_user = len(user)
    #print("총 채팅 참여자 수:", total_user)

    average = np.mean(np.array(count_u))

    # 오름차순으로 정렬한 후 10 번째로 많은 채팅 참여자 수를 구함
    sorted_list = sorted(count_u)
    max10th = sorted_list[-10]

    point = []
    for i in range(len(count_u)):
        if count_u[i] >= max10th:
            point.append((i, count_u[i]))

    #visualization(count_u)
    print_point_hhmmss(point)
    return point


def analyze1_minute(data, comment=None):#분단위로 쪼개고 해당 단위시간(분) 내에 가장 채팅이 많은 지점(초)을 리턴
    second = []
    if comment is None:
        # 채팅 기록에서 모든 comment의 시간 추출
        for i in range(len(data)):
            second.append(int(data[i][0]))
    else:
        # 채팅 기록에서 특정 comment가 포함된 채팅 시간 추출
        for i in range(len(data)):
            if comment in data[i][2]:
                second.append(int(data[i][0]))

    count = []
    for i in range(int(data[len(data) - 1][0]) + 1):
        count.append(0)

    for x in second:
        count[x] += 1

    minute = []
    cut = 0  # 60초 단위로 쪼개기 위한 변수
    while True:
        try:
            arr = count[cut:cut + 60]
            minute.append((arr.index(max(arr)) + cut, max(arr)))  # (시간(초),채팅량) 튜플로 저장
            cut += 60
        except:
            break

    minute.sort(key=lambda ele: ele[1], reverse=True)
    point = minute[0:3]
    point.sort(key=lambda ele: ele[0])

    print_point_hhmmss(point)
    return point


def analyze1_sound(volume):
    minute = []
    for i in range(len(volume)):
        minute.append((i,volume[i]))

    minute.sort(key=lambda ele: ele[1], reverse=True)
    point = minute[0:3]
    point.sort(key=lambda ele: ele[0])

    print_point_hhmm(point)
    return point


def find_high_frequency_words(data, n=10.0, m=10.0):
    freq = {}
    time = {}
    for i in range(len(data)):
        nouns = okt.nouns(data[i][2])
        nouns = set(nouns)
        for key in nouns:
            if len(key) < 2:
                continue
            elif key in freq.keys():
                freq[key] += 1
                time[key].append(data[i][0])
            else:
                freq[key] = 1
                time[key] = [data[i][0]]

    sorted_freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)

    section = {}
    for i in range(len(sorted_freq)):
        if len(section) == 10 or sorted_freq[i][1] < m:
            break
        key = sorted_freq[i][0]
        start_time = time[key][0]
        count = 1
        for j in range(1, len(time[key])):
            if time[key][j] - time[key][j-1] > n:
                if count >= m:
                    end_time = time[key][j-1]
                    if key in section.keys():
                        section[key].append([start_time, end_time])
                    else:
                        section[key] = [[start_time, end_time]]
                start_time = time[key][j]
                count = 1
            else:
                count += 1

    top_10 = []
    if len(section) == 10:
        i = 0
        for key in section.keys():
            if i == 10:
                break
            else:
                top_10.append([key, freq[key], section[key]])
                i += 1
        print_section_hhmmss(top_10)
    else:
        top_10 = find_high_frequency_words(data, n+1.0, m-0.5)
    return top_10