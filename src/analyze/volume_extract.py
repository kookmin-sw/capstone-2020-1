import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from moviepy.audio.fx.all import *
from moviepy.editor import *


def save_graph(platform, videoID, volumes, avg):
    plt.switch_backend('Agg')
    fig, ax1 = plt.subplots()  # plot
    ax1.plot(np.linspace(0, len(volumes), len(volumes)), volumes, color='b')
    plt.axhline(y=avg, color='r', linewidth=1)
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


# 여러 영상들과 비교해서 평준화 함수
def global_normalize(platform, videoID, volumesPerMinute,
                     avg_list):  # 인자 : AudioFileClip으로 읽은 audio 데이터, sound_extract의 리턴값, 여러 영상들의 소리 평균값이 저장된 list
    audio = load_audio(platform, videoID)

    global_avg = np.mean(avg_list)  # 여러 영상들 평균값

    volumesPerMinute.sort(reverse=True)
    upper_volume = volumesPerMinute[0:int(
        len(volumesPerMinute) / 3)]  # 분 단위로 저장되어 있는 max값들 중 상위 1/3 추출 (작은 소리도 평균에 집계되면 소리가 너무 커질 수 있으므로)

    avg = np.mean(upper_volume)  # 본 영상 평균값

    audio = audio.volumex(global_avg / avg)  # 평균값으로 맞춤

    path = "./audio/normalizeAudio/"

    if not os.path.exists(path):
        os.makedirs(path)

    audio.write_audiofile(path + f"{platform}_{videoID}.wav")  # file write

    return audio, avg


# volumesPerMinute 그래프 + 적정 volume level을 표시하여 저장
def local_normalize(platform, videoID, volumesPerMinute):
    avg = np.mean(volumesPerMinute)  # sound_extract에서 얻은 volumesPerMinute을 평균냄

    save_graph(platform, videoID, volumesPerMinute, 0.2)

    return avg


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
    for i in range(0, len(volumes), 60):  # 60초 단위로 쪼개서 단위 시간 내 가장 큰 값 추출, (2)시간 오래
        if len(volumes) - i < 60:
            volumesPerMinute.append(max(volumes[i:len(volumes)]))
        else:
            volumesPerMinute.append(max(volumes[i:i + 60]))

    if filetype == "video":
        video.close()
    elif filetype == "audio":
        audio.close()
    return volumesPerMinute
