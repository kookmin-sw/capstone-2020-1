import os
import re
import youtube_dl
# pip3 install youtube-dl


def download(platform, videoID, url):
    dw_opts = {'format': 'worstaudio/worst', 'extractaudio': True, 'audioformat': "mp3",
               'outtmpl': "audio/" + platform + '_' + videoID + '_' + '%(playlist_index)s' + ".mp3"}
    try:
        with youtube_dl.YoutubeDL(dw_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print('error', e)
    print('Finish!')


if __name__ == '__main__':
    url = input("stream url : ")

    if "afree" in url:
        platform = "AfreecaTV"
        if "afreecatv" in url:
            url = re.search(r"http://vod.afreecatv.com/PLAYER/STATION/[0-9]+", url).group()
        videoID = url.split('/')
        videoID = videoID[-1]
    elif "twitch" in url:
        platform = "Twitch"
        url = re.search(r"https://www.twitch.tv/videos/[0-9]+", url).group()
        videoID = url.split('/')
        videoID = videoID[-1]
    elif "youtu" in url:
        platform = "Youtube"
        if 'youtube' in url:
            url = re.search(r"https://www.youtube.com/watch\?v=[a-zA-Z0-9_-]+", url).group()
            videoID = url.split('=')
        else:
            url = re.search(r"https://youtu.be/[a-zA-Z0-9_-]+", url).group()
            videoID = url.split('/')
        videoID = videoID[-1]

    if not os.path.exists("./audio"):
        os.makedirs("./audio")
    print(id)
    if platform + '_' + videoID + '_' + '1' + ".mp3" in os.listdir("./audio"):
        print ('This audio file has already been requested.')
    else:
        download(platform, videoID, url)