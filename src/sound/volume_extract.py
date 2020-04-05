import sys
from moviepy.editor import *
import librosa
import os
import numpy as np
import matplotlib.pyplot as plt
import time

def sound_extract(filename):
    start = time.time()
    video = VideoFileClip(filename)
    audio = video.audio

    sr = audio.fps # 샘플링 레이트
    cut = lambda x: audio.subclip(x, x+1).to_soundarray(fps=sr)#time series
    volume = lambda array: np.sqrt(((1.0*array)**2).mean())
    volumes = [volume(cut(i)) for i in range(0, int(audio.duration-2))]
    
    """
    fig, ax1 = plt.subplots() # plot
    ax1.plot(np.linspace(0, len(volumes), len(volumes)), volumes, color = 'b')
    ax1.set_ylabel("Volume") # y 축
    ax1.set_xlabel("Second") # x 축
    plt.title("Volumes of each second") # 제목
    plt.show()
    """
    
    video.close()
    
    return volumes

def get_peak_point(mag_s, time):
    # 영상을 10분 단위로 분석하기 위한 변수
    cut = 0

    Highlight = []
    while (cut < len(mag_s)):
        MAX = 0
        TIME = 0

        # 소리의 크기가 가장 커지는 부분의 시간과 크기를 저장함
        for i in range(cut, cut + 600):
            try:
                if (mag_s[i] > MAX):
                    MAX = mag_s[i]
                    TIME = i
            except:
                break
                
        Highlight.append((TIME,MAX))
        
        cut += 600
                
    return Highlight
    
def get_peak_point2(mag_s, time):
    #전체를 살펴보고 1~10순위 출력
    arr=[]
    for i in range(len(mag_s)):
        arr.append((time[i],mag_s[i]))
    
    arr.sort(key = lambda ele : ele[1],reverse=True)
    
    Highlight = arr[0:100]
    Highlight.sort(key = lambda ele : ele[0])
                
    return Highlight
                
def print_highlight(Highlight_arr):
        for i in Highlight_arr:
            Highlight = int(i[0])
            minute = Highlight // 60
            hour = minute // 60
            minute = minute % 60
            second = Highlight % 60
            print(str(hour) + ":" + str(minute) + ":" + str(second))  # 시:분:초 로 표기