import sys

import volume_extract
import numpy as np
from twitch_afreeca import analysis
from twitch_afreeca import download

file_name = sys.argv[1]
volumes = volume_extract.sound_extract(file_name)
highlight = volume_extract.get_peak_point2(volumes, np.linspace(0, len(volumes), len(volumes)))
volume_extract.print_highlight(highlight)
"""
afreeca_videoID = "558092842"
afreeca_chat = download.afreeca(afreeca_videoID)
afreeca_point1 = analysis.analyze1(afreeca_chat) # 초당 채팅량 분석 후 상위 10개 지점 출력(상위10위 지점이 여러개면 10개 이상 출력함)
"""

twitch_videoID = "558092842"
twitch_chat = download.twitch(twitch_videoID)
twitch_point1 = analysis.analyze1(twitch_chat)
