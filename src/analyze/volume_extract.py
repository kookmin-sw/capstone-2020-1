import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import time
from moviepy.audio.fx.all import *
from moviepy.editor import *

# 여러 영상들과 비교해서 평준화 함수
def global_normalize(audio, volumesPerMinute, avg_list): # 인자 : AudioFileClip으로 읽은 audio 데이터, sound_extract의 리턴값, 여러 영상들의 소리 평균값이 저장된 list
    global_avg = np.mean(avg_list) # 여러 영상들 평균값
    
    volumesPerMinute.sort(reverse=True) 
    upper_volume = volumesPerMinute[0:int(len(volumesPerMinute)/3)] # 분 단위로 저장되어 있는 max값들 중 상위 1/3 추출 (작은 소리도 평균에 집계되면 소리가 너무 커질 수 있으므로)
    
    avg = np.mean(upper_volume) # 본 영상 평균값
    
    audio = audio.volumex(global_avg / avg) # 평균값으로 맞춤
    
    audio.write_audiofile("global_tmp.wav") # file write
    
    return audio, avg

# 영상 내 소리 평준화 함수
def local_normalize(audio, volumesPerMinute): # 인자 : AudioFileClip으로 읽은 audio 데이터, sound_extract의 리턴값
    fragment = [] # 1분 단위로 분할
    for i in range(0, int(audio.duration), 60):
        if(int(audio.duration)-i < 60):
            fragment.append(audio.subclip(i,int(audio.duration)))
        else:
            fragment.append(audio.subclip(i,i+60))
    
    avg = np.mean(volumesPerMinute) # sound_extract에서 얻은 volumesPerMinute을 평균냄
    
    for i in range(len(volumesPerMinute)): # 1분 단위로 분할한 조각들을 평균값으로 맞춤
        power = avg / volumesPerMinute[i]
        #print(i,":",power)
        fragment[i] = fragment[i].volumex(power)
    
    merged = concatenate_audioclips(fragment)
    
    merged.write_audiofile("local_tmp.wav") # file write
    
    return merged, avg
    
    #audio = volumex(audio, 2.0)
    #audio = audio.fx( volumex, 0.5) # half audio, use with fx
    

def sound_extract(platform, videoID, filetype="audio"):
    start = time.time()
    if(filetype == "video"):
        files = []
        for i in os.listdir('./video/'):
            if platform+'_'+videoID in i:
                files.append(i)
        video_arr = []
        for filename in files:
            video_arr.append(VideoFileClip("video/"+filename))
        video = concatenate_videoclips(video_arr)
        audio = video.audio
    elif(filetype == "audio"):
        files = []
        for i in os.listdir('./audio/'):
            if platform+'_'+videoID in i:
                files.append(i)
        audio_arr = []
        for filename in files:
            audio_arr.append(AudioFileClip("audio/"+filename))
        audio = concatenate_audioclips(audio_arr)

    sr = audio.fps # 샘플링 레이트
    cut = lambda x: audio.subclip(x, x+1).to_soundarray(fps=sr)#time series
    volume = lambda array: np.sqrt(((1.0*array)**2).mean())
    volumes = [volume(cut(i)) for i in range(0, int(audio.duration-2))]
    volumesPerMinute=[]
    for i in range(0, len(volumes), 60):
        if(len(volumes) - i < 60 ):
            volumesPerMinute.append(max(volumes[i:len(volumes)]))
        else:
            volumesPerMinute.append(max(volumes[i:i+60]))    

    if(filetype == "video"):
        video.close()
    elif(filetype == "audio"):
        audio.close()
    return volumesPerMinute
