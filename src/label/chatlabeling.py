import os

path = './chatlog/'
path2 = './result/'
filename = 'am1.txt'

if not os.path.exists("./result"):
    os.makedirs("./result")

put = ""
n = 0
lines = []
with open(path2 + 'labeling_' + filename, 'a', encoding='utf-8') as f:
    with open(path + filename, 'r', encoding='utf-8') as t:
        lines = t.readlines()
        for line in lines:
            if line == '':
                continue
            line = line.replace("\n", "")
            print(line)
            while True:
                put = input("긍정 1 부정 0 중지 q:")
                if put == '1':
                    break
                elif put == '0':
                    break
                elif put == 'q':
                    break
            if put == 'q':
                break
            result = line + '\t' + put + '\n'
            f.write(result)
            n += 1
    t.close()
f.close()

with open(path + filename, 'w', encoding='utf-8') as t:
    t.writelines((lines[n:]))