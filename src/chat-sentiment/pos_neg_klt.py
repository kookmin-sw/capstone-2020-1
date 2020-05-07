import json
import os
from pprint import pprint
import nltk
import numpy as np
import time
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
from tensorflow.keras.models import load_model
import os

chatlogFolder = '../download/chatlog/'
chatlogFileName = 'AfreecaTV_46443514_klt.txt'

print('Load dataset')

def read_data(filename, flag=False):
    with open(filename, 'r', encoding='cp949') as f:
        if flag:
            data = [line.split('\t')[1:] for line in f.read().splitlines()]
            data = data[1:]
        else:
            data = [line.split('\t') for line in f.read().splitlines()]
    return data

path = './'
train_data = read_data(path + 'train_klt.txt', True)
train_data += read_data(path + 'chat_train_klt.txt')
for i in train_data:
    if len(i) != 2:
        print(i)
test_data = read_data(path + 'chat_test_klt.txt')

print('Preprocessing')

if os.path.isfile('train_docs_klt.json'):
    with open('train_docs_klt.json', encoding='utf-8') as f:
        train_docs = json.load(f)
    with open('test_docs_klt.json', encoding='utf-8') as f:
        test_docs = json.load(f)
else:
    train_docs = []
    for row in train_data:
        with open('temp.txt', 'wt', encoding='euc-kr') as f:
            f.write(row[0])
        temp = []
        temp = os.popen('kma.exe -sw1i+p temp.txt').read().replace('> + (', '>\n(').replace('\t', '').replace(') (', ')\n(').split('\n')
        train_docs += [(temp[0:-1], row[1])]
    test_docs = []
    for row in test_data:
        with open('temp.txt', 'wt', encoding='cp949') as f:
            f.write(row[0])
        temp = []
        temp = os.popen('kma.exe -sw1i+p temp.txt').read().replace('> + (', '>\n(').replace('\t', '').replace(') (', ')\n(').split('\n')
        test_docs += [(temp[0:-1], row[1])]
    os.remove('temp.txt')
    # JSON 파일로 저장

    with open(path+'train_docs_klt.json', 'wt', encoding="utf-8") as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
    with open(path+'test_docs_klt.json', 'wt', encoding="utf-8") as make_file:
        json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")

tokens = [t for d in train_docs for t in d[0]]

text = nltk.Text(tokens, name='NMSC')
selected_words_num = 5000
selected_words = [f[0] for f in text.vocab().most_common(selected_words_num)]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]
    

train_x = [term_frequency(d) for d, _ in train_docs]
test_x = [term_frequency(d) for d, _ in test_docs]
train_y = [c for _, c in train_docs]
test_y = [c for _, c in test_docs]

x_train = np.asarray(train_x).astype('float32')
x_test = np.asarray(test_x).astype('float32')

y_train = np.asarray(train_y).astype('float32')
y_test = np.asarray(test_y).astype('float32')

print('Model define and train')

epoch = 10
if not os.path.isfile('spm_sentiment_model'+str(selected_words_num)+'_'+str(epoch)+'.h5'):
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(selected_words_num,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=optimizers.RMSprop(lr=0.001),
                loss=losses.binary_crossentropy,
                metrics=[metrics.binary_accuracy])
    model.fit(x_train, y_train, epochs=epoch, batch_size=512)
    results = model.evaluate(x_test, y_test, batch_size=512)
    print('정확도: ', results[1])
    model.save('spm_sentiment_model'+str(selected_words_num)+'_'+str(epoch)+'.h5')
else:
    model = load_model('spm_sentiment_model'+str(selected_words_num)+'_'+str(epoch)+'.h5')
    results = model.evaluate(x_test, y_test, verbose=0)
    print('정확도: ', results[1])

def predict_pos_neg(review):
    with open('temp.txt', 'w', encoding='cp949') as f:
        f.write(review)
    token = os.popen('kma.exe -sw1i+p temp.txt').read().replace('> + (', '>\n(').replace('\t', '').replace(') (', ')\n(').split('\n')
    token = token[0:-1]
    os.remove('temp.txt')
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
    score = float(model.predict(data))
    with open(str(selected_words_num)+'_'+str(epoch)+'_KLT_'+chatlogFileName, 'a', encoding='cp949') as f:
        if(score > 0.2):
            f.write("[{}]는 긍정\n".format(review))
        else:
            f.write("[{}]는 부정\n".format(review))

# print('Real data inference')

# start = time.time()
# with open(chatlogFolder+chatlogFileName, 'r', encoding='cp949') as f:
#     chatlog = [line.split('\t') for line in f.read().splitlines()]
# for c in chatlog:
#     predict_pos_neg(c[2])
# print("소요시간: ", time.time()-start)