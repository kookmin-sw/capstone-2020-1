# import os
# import json
# with open("sample.txt", 'r', encoding='utf-8') as f:
#     data = [line.split('\t')[1:] for line in f.read().splitlines()]
#     data = data[1:]
# print(data)
# train_docs=[]
# for d in data:
#     with open('temp.txt', 'w') as f:
#         f.write(d[0])
#     temp = []
#     temp = os.popen('kma.exe -sw1i+p temp.txt').read().replace('> + (', '>\n(').replace('\t', '').split('\n')
#     train_docs += [(temp, d[1])]
#     print(temp)
# with open('train_docs_klt.json', 'w', encoding="utf-8") as make_file:
#     json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
# # temp = os.popen('kma.exe -sw \n 나는 바보다').read()
# # print(temp)0
train_docs=["가", "나"]
train_docs[0].encode('utf-8')
print(train_docs)
print(type(train_docs[0]))
print(type(train_docs[1]))