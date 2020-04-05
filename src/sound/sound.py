import sys
from moviepy.editor import *

import librosa
import os
import numpy as np
import matplotlib.pyplot as plt

def sound_extract(filename):
    # 영상으로부터 오디오 추출
    # 부산물인 tmp.wav가 생성되지 않도록 수정
    video = VideoFileClip(filename)
    audio = video.audio

    sr = audio.fps#샘플링 레이트
    mag = audio.to_soundarray(fps=sr)#time series
    channel = audio.nchannels#소리 채널

    #print(len(mag))
    #print(sr*audio.end)

    #sr만큼 샘플링된 소리 데이터들을 단위 시간(s) 당 평균으로 계산한다.
    mag_s = []#단위 시간(s)당 평균 소리 크기를 담을 리스트
    while ( len(mag_s) < audio.end ):
        try:
            mag_sum = 0
            for i in range(len(mag_s)*sr , len(mag_s)*sr + sr):
                mag_sum += mag[i][0]#해당 시간의 모든 채널값들의 평균이나, 채널 하나가지고 한 거나 비슷해서 일단 채널 하나만 가지고 계산
            mag_s.append(mag_sum / sr)
            print("processing ",len(mag_s))
        except:
            break
            
    time = np.linspace(0, len(mag_s), len(mag_s))
            
    """
    #스펙트럼
    fig, ax1 = plt.subplots() # plot
    ax1.plot(time, mag_s, color = 'b', label='waveform')
    ax1.set_ylabel("Amplitude") # y 축
    ax1.set_xlabel("Time [s]") # x 축
    plt.title("hh") # 제목
    plt.show()
    """
    
    return mag_s, time

def get_peak_point(mag_s, time):
    # 영상을 10분 단위로 분석하기 위한 변수
    cut = 0

    while (cut < len(mag_s)):
        MAX = 0
        Highlight = 0

        # 소리의 크기가 가장 커지는 부분의 시간과 크기를 저장함
        for i in range(cut, cut + 600):
            try:
                if (mag_s[i] > MAX):
                    MAX = mag_s[i]
                    Highlight = time[i]
            except:
                break

        Highlight = int(Highlight)
        print(MAX, str(Highlight // 60) + ":" + str(Highlight % 60))  # 분:초 로 표기

        cut += 600

#mag, time = sound_extract("kimdoe.mp4")
#get_peak_point(mag, time)