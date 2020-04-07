from . import video
from . import audio
from . import chatlog

while True:
    opt = input("채팅다운: 'c', 비디오다운: 'v', 오디오다운: 'a'")
    if opt == 'c':
        chatlog.main()
        break
    elif opt == 'v':
        video.main()
        break
    elif opt == 'c':
        audio.main()
        break
    else:
        continue
