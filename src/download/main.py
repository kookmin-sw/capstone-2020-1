from . import video
from . import audio
from . import chatlog

while True:
    opt = input("채팅다운: 'c', 비디오다운: 'v', 오디오다운: 'a'")
    if opt == 'c':
        chatlog()
        break
    elif opt == 'v':
        video()
        break
    elif opt == 'c':
        audio()
        break
    else:
        continue
