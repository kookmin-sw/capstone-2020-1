import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from moviepy.audio.fx.all import *
from moviepy.editor import *


# volumesPerMinute 그래프 + 적정 volume level을 표시하여 저장
def save_graph(platform, videoID, volumes, time_range=30, AVG_20=0.221829165):  # AVG_20 = 유튜브 하이라이트 영상 20개에 대한 평균
    plt.switch_backend('Agg')
    fig, ax1 = plt.subplots()  # plot
    x = list(range(len(volumes)))
    for i in range(len(x)):
        x[i] *= time_range
    ax1.plot(x, volumes, color='b')
    plt.axhline(y=AVG_20, color='r', linewidth=1)
    ax1.set_ylabel("Volume")  # y 축
    ax1.set_xlabel("second")  # x 축
    plt.title("Volumes of each second")  # 제목

    path = "./audio/normalizeAudio/"
    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path + f"{platform}_{videoID}.png")


def load_audio(platform, videoID, filetype):
    files = []
    for i in os.listdir('./' + filetype + '/'):
        if platform + '_' + videoID in i:
            files.append(i)

    arr = []

    if filetype == "video":
        for filename in files:
            arr.append(VideoFileClip("video/" + filename))
        video = concatenate_videoclips(arr)
        audio = video.audio
        video.close()
    elif filetype == "audio":
        for filename in files:
            arr.append(AudioFileClip("audio/" + filename))  # 음성 파일 로드
        audio = concatenate_audioclips(arr)  # 음성 파일이 분할된 상태라면 이어붙임

    return audio


def sound_extract(platform, videoID, time_range=30, filetype="audio"):
    audio = load_audio(platform, videoID, filetype)

    sr = audio.fps  # 샘플링 레이트
    cut = lambda x: audio.subclip(x, x + 1).to_soundarray(fps=sr)  # 1초에 해당하는 데이터를 뽑는 람다함수
    volume = lambda array: np.sqrt(((1.0 * array) ** 2).mean())  # 음압 -> 음량 변환하는 람다함수

    volumes = []
    for i in range(0, int(audio.duration - 2)):  # audio에 대해 람다함수 실행
        try:  # 간혹 분할되어 다운된 영상에 대해 발생하는 예외 처리..
            volumes.append(volume(cut(i)))
        except:
            volumes.append(0.0)

    volumesPerMinute = []
    for i in range(0, len(volumes), time_range):  # time_range 초 단위로 쪼개서 단위 시간 내 가장 큰 값 추출
        if len(volumes) - i < time_range:
            volumesPerMinute.append(max(volumes[i:len(volumes)]))
        else:
            volumesPerMinute.append(max(volumes[i:i + time_range]))

    audio.close()
    return volumesPerMinute
