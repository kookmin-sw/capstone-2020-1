import os
import re
import video
import audio
import chatlog
import volume_extract as sound
import analysis


url = input("stream url : ")
platform = ""
videoID = ""

if "afree" in url:
    # AfreecaTV 주소형식
    # http://vod.afreecatv.com/PLAYER/STATION/videoID
    # http://v.afree.ca/ST/videoID
    platform = "AfreecaTV"
    if "afreecatv" in url:
        url = re.search(r"http://vod.afreecatv.com/PLAYER/STATION/[0-9]+", url).group()
    else:
        url = re.search(r"http://v.afree.ca/ST/[0-9]+", url).group()
    videoID = url.split('/')
    videoID = videoID[-1]
elif "twitch" in url:
    # Twitch 주소형식
    # https://www.twitch.tv/videos/videoID
    platform = "Twitch"
    url = re.search(r"https://www.twitch.tv/videos/[0-9]+", url).group()
    videoID = url.split('/')
    videoID = videoID[-1]
elif "youtu" in url:
    # Youtube 주소형식
    # https://www.youtube.com/watch?v=videoID
    # https://youtu.be/videoID
    platform = "Youtube"
    if 'youtube' in url:
        url = re.search(r"https://www.youtube.com/watch\?v=[a-zA-Z0-9_-]+", url).group()
        videoID = url.split('=')
    else:
        url = re.search(r"https://youtu.be/[a-zA-Z0-9_-]+", url).group()
        videoID = url.split('/')
    videoID = videoID[-1]

"""
if not os.path.exists("./video"):
    os.makedirs("./video")
if platform+"_"+videoID+".mp4" in os.listdir("./video"):
    print('This video file has already been requested.')
    volume = sound.sound_extract(platform, videoID, "video")
else:
    video.download(platform, videoID, url)
    volume = sound.sound_extract(platform, videoID, "video")
"""

if not os.path.exists("./audio"):
    os.makedirs("./audio")
if platform + "_" + videoID + ".mp3" in os.listdir("./audio"):
    print('This audio file has already been requested.')
    volume = sound.sound_extract(platform, videoID)
    print("< audio point >")
    audio_point = analysis.analyze1_sound(volume)
else:
    audio.download(platform, videoID, url)
    volume = sound.sound_extract(platform, videoID)
    print("< audio point >")
    audio_point = analysis.analyze1_sound(volume)

if not os.path.exists("./chatlog"):
    os.makedirs("./chatlog")
if platform + "_" + videoID + ".txt" in os.listdir("./chatlog"):
    print('This chatlog file has already been requested.')
    chat_data = chatlog.download(platform, videoID)
    print("< chatlog point >")
    chat_point = analysis.analyze1_minute(chat_data)
else:
    chat_data = chatlog.download(platform, videoID)
    print("< chatlog point >")
    chat_point = analysis.analyze1_minute(chat_data)


