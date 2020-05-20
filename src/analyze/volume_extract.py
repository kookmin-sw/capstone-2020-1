import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from moviepy.audio.fx.all import *
from moviepy.editor import *


# volumesPerMinute 그래프 + 적정 volume level을 표시하여 저장
def save_graph(platform, videoID, volumes, AVG_20=0.221829165):  # AVG_20 = 유튜브 하이라이트 영상 20개에 대한 평균
    plt.switch_backend('Agg')
    fig, ax1 = plt.subplots()  # plot
    x = list(range(len(volumes)))
    for i in range(len(x)):
        x[i] *= 30
    ax1.plot(x, volumes, color='b')
    plt.axhline(y=AVG_20, color='r', linewidth=1)
    ax1.set_ylabel("Volume")  # y 축
    ax1.set_xlabel("minute")  # x 축
    plt.title("Volumes of each minute")  # 제목

    path = "./audio/normalizeAudio/"
    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path + f"{platform}_{videoID}.png")


def load_audio(platform, videoID):
    files = []
    for i in os.listdir('./audio/'):
        if platform + '_' + videoID in i:
            files.append(i)
    audio_arr = []
    for filename in files:
        audio_arr.append(AudioFileClip("audio/" + filename))
    return concatenate_audioclips(audio_arr)


def sound_extract(platform, videoID, filetype="audio"):
    if filetype == "video":
        files = []
        for i in os.listdir('./video/'):
            if platform + '_' + videoID in i:
                files.append(i)
        video_arr = []
        for filename in files:
            video_arr.append(VideoFileClip("video/" + filename))
        video = concatenate_videoclips(video_arr)
        audio = video.audio
    elif filetype == "audio":
        audio = load_audio(platform, videoID)

    sr = audio.fps  # 샘플링 레이트
    cut = lambda x: audio.subclip(x, x + 1).to_soundarray(fps=sr)  # 1초에 해당하는 데이터를 뽑는 람다함수
    volume = lambda array: np.sqrt(((1.0 * array) ** 2).mean())  # 음압 -> 음량 변환하는 람다함수
    volumes = [volume(cut(i)) for i in range(0, int(audio.duration - 2))]  # audio에 대해 람다함수 실행, (1)시간 오래
    volumesPerMinute = []
    time_range = 30
    for i in range(0, len(volumes), time_range):  # time_range 초 단위로 쪼개서 단위 시간 내 가장 큰 값 추출, (2)시간 오래
        if len(volumes) - i < time_range:
            volumesPerMinute.append(max(volumes[i:len(volumes)]))
        else:
            volumesPerMinute.append(max(volumes[i:i + time_range]))

    if filetype == "video":
        video.close()
    elif filetype == "audio":
        audio.close()
    return volumesPerMinute
