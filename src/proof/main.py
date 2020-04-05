import download
import volume_extract as sound

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
# afreeca_videoID = "54055792"
# download.afreeca(afreeca_videoID)

# twitch_videoID = "562644795"
# download.twitch(twitch_videoID)

# youtube_videoID = "VUzT3OEPtQk"
# download.youtube(youtube_videoID)

# 영상에서 초당 소리의 크기 시각화
volume = sound.sound_extract("full.mp4")
print(sum(volume)/len(volume))
volume = sound.sound_extract("highlight.mp4")
print(sum(volume)/len(volume))

