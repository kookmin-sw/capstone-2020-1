import numpy as np
import matplotlib.pyplot as plt


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