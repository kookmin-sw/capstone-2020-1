import youtube_dl
import ffmpeg
import os
# 사용전 pip3 install youtube-dl

def download_video_twitch(video_list):
    for video_url in video_list:

        if not os.path.exists("./download"):
            os.makedirs("./download")
        download_path = os.path.join('./download', '%(title)s.%(ext)s')

        dw_opts = {'format' : '360p/360p',
                   'outtmpl' : download_path}

        t = 0
        while t == 0:
            try:
                with youtube_dl.YoutubeDL(dw_opts) as ydl:
                    t = 1
                    ydl.download([video_url])
            except Exception as e:
                t = 0
                print('error', e)

def download_video_afreeca(video_list):
    for video_url in video_list:

        if not os.path.exists("./download"):
            os.makedirs("./download")
        download_path = os.path.join('./download', '%(title)s.%(ext)s')

        dw_opts = {'extension':'mp4',
                   'resolution':'960x540',
                   'outtmpl' : download_path}

        t = 0
        while t == 0:
            try:
                with youtube_dl.YoutubeDL(dw_opts) as ydl:
                    t = 1
                    ydl.download([video_url])
            except Exception as e:
                t = 0
                print('error', e)

def download_video_youtube(video_list):
    for video_url in video_list:

        if not os.path.exists("./download"):
            os.makedirs("./download")
        download_path = os.path.join('./download', '%(title)s.%(ext)s')

        dw_opts = {'format' : '134/140',
                   'extension' : 'mp4',
                   'outtmpl': download_path}
        try:
            with youtube_dl.YoutubeDL(dw_opts) as ydl:
                ydl.download([video_url])
        except Exception as e:
            print('error', e)

def main():

    url_list_a = []
    url_list_y = []
    url_list_t = []
    while True:
        url = input("영상주소를 입력하세요(그만 입력하려면 'q'를 눌러주세요):")
        if url == 'q':
            break
        else:
            if 'afreecatv' in url:
                url_list_a.append(url)
            elif 'youtube' in url:
                url_list_y.append(url)
            else:
                url_list_t.append(url)

    download_video_afreeca(url_list_a)
    download_video_twitch(url_list_t)
    download_video_youtube(url_list_y)



    print('Finish!')


