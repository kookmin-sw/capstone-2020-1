import numpy as np
import matplotlib.pyplot as plt
import download


def print_point(second):
    minute = int(second / 60)
    if minute >= 60:
        hour = int(minute / 60)
        minute %= 60
    else:
        hour = int(minute / 60)
    second = int(second % 60)
    print(download.double_digit(hour) + ':' + download.double_digit(minute) + ':' + download.double_digit(second))


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

    chk = []
    for x in range(len(count)):
        chk.append(average)

    # 오름차순으로 정렬한 후 10 번째로 많은 채팅 수를 구함
    max10th = sorted(count)[-100]

    point = []
    print("편집점:")
    for i in range(len(count)):
        if count[i] >= max10th:
            point.append(i)
            print_point(i)

    """
    plt.bar(range(len(count)), count)  # 채팅 수
    # plt.twinx()
    # plt.plot(range(len(count)), chk, 'r--')  # 평균
    plt.xlabel("second")
    plt.ylabel("chat / second")
    plt.show()
    """
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
    total_user = len(user)
    del user
    print("총 채팅 참여자 수:", total_user)

    average = np.mean(np.array(count_u))

    chk = []
    for x in range(len(count_u)):
        chk.append(average)

    # 오름차순으로 정렬한 후 10 번째로 많은 채팅 참여자 수를 구함
    max10th = sorted(count_u)[-10]

    point = []
    print("편집점:")
    for i in range(len(count_u)):
        if count_u[i] >= max10th:
            point.append(i)
            print_point(i)
    return point
    plt.bar(range(len(count_u)), count_u)  # 채팅 참여자 수
    # plt.twinx()
    # plt.plot(range(len(count)), chk, 'r--')  # 평균
    plt.xlabel("second")
    plt.ylabel("chat / second")
    plt.show()


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
    cut = 0#60초 단위로 쪼개기 위한 변수
    while True:
        try:
            arr = count[cut:cut+60]
            minute.append( (arr.index(max(arr)) + cut,max(arr)) )#(시간(초),채팅량) 튜플로 저장
            cut += 60
        except:
            break
            
    minute.sort(key = lambda ele : ele[1],reverse=True)
    highlight = minute[0:10]
    highlight.sort(key = lambda ele : ele[0])
    
    for i in range(len(highlight)):
        print_point( highlight[i][0] )
    
    return minute
    
def analyze1_sound(volume):
    arr = []
    for i in range(len(volume)):
        arr.append( (i,volume[i])  )
        
    arr.sort(key = lambda ele : ele[1],reverse=True)
    highlight = arr[0:10]
    highlight.sort(key = lambda ele : ele[0])
    for i in highlight:
        print(i[0])