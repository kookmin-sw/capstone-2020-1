import download
import volume_extract as sound
import analysis
import sys

"""
[참고 사이트]
- 아프리카
https://www.afreecatv.com/player/Player.xml
https://cafe.naver.com/tsoul7/74753
https://github.com/minkyoJang/WD_AI-BigData
- 트위치
https://github.com/mcpcseal/TwitchChatAnalyzer
https://nbviewer.jupyter.org/github/tark1998/twitch-searching-highlight-through-comments-counting/tree/master/
https://steemit.com/kr-dev/@steemonen1/twitch
"""


# # videoID로 초당 채팅 수 시각화
afreeca_videoID = "54518239"
afreeca_chat = download.afreeca(afreeca_videoID)
afreeca_point1 = analysis.analyze1_minute(afreeca_chat)

"""
twitch_videoID = "568292071"
twitch_chat = download.twitch(twitch_videoID)
twitch_point1 = analysis.analyze1_minute(twitch_chat)
"""

# youtube_videoID = "VUzT3OEPtQk"
# download.youtube(youtube_videoID)


# 영상에서 초당 소리의 크기 시각화
file_name = sys.argv[1]
volume = sound.sound_extract(file_name)
point = analysis.analyze1_sound(volume)

#print(sum(volume)/len(volume))


#volume = sound.sound_extract("highlight.mp4")
#print(sum(volume)/len(volume))

