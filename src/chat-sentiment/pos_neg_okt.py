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


chatlogFolder = '../download/chatlog/'
chatlogFileName = 'AfreecaTV_46443514.txt'

print('Load dataset')

def read_data(filename, flag=False):
    with open(filename, 'r', encoding='utf-8') as f:
        if flag:
            data = [line.split('\t')[1:] for line in f.read().splitlines()]
            data = data[1:]
        else:
            data = [line.split('\t') for line in f.read().splitlines()]
    return data

path = './'
train_data = read_data(path + 'train.txt', True)
train_data += read_data(path + 'chat_train.txt')
for i in train_data:
    if len(i) != 2:
        print(i)
test_data = read_data(path + 'chat_test.txt')

print('Preprocessing')


# Okt Tokenizer
okt = Okt()

def okt_tokenize(doc):
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

if os.path.isfile('train_docs.json'):
    with open('train_docs.json', encoding='utf-8') as f:
        train_docs = json.load(f)
    with open('test_docs.json', encoding='utf-8') as f:
        test_docs = json.load(f)
else:
    train_docs = []
    train_docs += [(okt_tokenize(row[0]), row[1]) for row in train_data]
    test_docs = [(okt_tokenize(row[0]), row[1]) for row in test_data]
    # JSON 파일로 저장
    with open(path+'train_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
    with open(path+'test_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")

tokens = [t for d in train_docs for t in d[0]]

text = nltk.Text(tokens, name='NMSC')
selected_words_num = 5000
selected_words = [f[0] for f in text.vocab().most_common(selected_words_num)]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]
    

# Okt Tokenizer
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
    token = okt_tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
    score = float(model.predict(data))
    with open(str(selected_words_num)+'_'+str(epoch)+'_Okt_'+chatlogFileName, 'a', encoding='utf-8') as f:
        if(score > 0.2):
            f.write("[{}]는 긍정\n".format(review))
        else:
            f.write("[{}]는 부정\n".format(review))

print('Real data inference')

start = time.time()
with open(chatlogFolder+chatlogFileName, 'r', encoding='utf-8') as f:
    chatlog = [line.split('\t') for line in f.read().splitlines()]
for c in chatlog:
    predict_pos_neg(c[2])
print("소요시간: ", time.time()-start)