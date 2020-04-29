from konlpy.tag import Okt
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
import sentencepiece as spm


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

# SPM Tokenizer
templates= '--input={} \
--pad_id={} \
--bos_id={} \
--eos_id={} \
--unk_id={} \
--model_prefix={} \
--vocab_size={} \
--character_coverage={} \
--model_type={}'
spm_train=''
for row in train_data:
    spm_train += row[0]+'\n'
with open('./spm_train.txt', 'w', encoding='utf-8') as f:
    f.write(spm_train)
if not os.path.isfile('spm_tokenizer.model'):
    train_input_file = "./spm_train.txt"
    pad_id=0  #<pad> token을 0으로 설정
    vocab_size = 10000 # vocab 사이즈
    prefix = 'spm_tokenizer' # 저장될 tokenizer 모델에 붙는 이름
    bos_id=1 #<start> token을 1으로 설정
    eos_id=2 #<end> token을 2으로 설정
    unk_id=3 #<unknown> token을 3으로 설정
    character_coverage = 1.0 # to reduce character set 
    model_type ='word' # Choose from unigram (default), bpe, char, or word

    cmd = templates.format(train_input_file,
                    pad_id,
                    bos_id,
                    eos_id,
                    unk_id,
                    prefix,
                    vocab_size,
                    character_coverage,
                    model_type)

    spm.SentencePieceTrainer.Train(cmd)

sp=spm.SentencePieceProcessor()
sp.Load('spm_tokenizer.model')
# sp.SetEncodeExtraOptions('bos:eos') # 문장 시작, 끝 기호 표시

def spm_tokenize(doc):
    return sp.EncodeAsPieces(doc)

if os.path.isfile('train_docs_spm.json'):
    with open('train_docs_spm.json', encoding='utf-8') as f:
        train_docs_spm = json.load(f)
    with open('test_docs_spm.json', encoding='utf-8') as f:
        test_docs_spm = json.load(f)
else:
    train_docs_spm = []
    train_docs_spm += [(spm_tokenize(row[0]), row[1]) for row in train_data]
    test_docs_spm = [(spm_tokenize(row[0]), row[1]) for row in test_data]
    # JSON 파일로 저장
    with open(path+'train_docs_spm.json', 'w', encoding="utf-8") as make_file:
        json.dump(train_docs_spm, make_file, ensure_ascii=False, indent="\t")
    with open(path+'test_docs_spm.json', 'w', encoding="utf-8") as make_file:
        json.dump(test_docs_spm, make_file, ensure_ascii=False, indent="\t")

tokens = [t for d in train_docs_spm for t in d[0]]

text = nltk.Text(tokens, name='NMSC')
selected_words_num = 5000
selected_words = [f[0] for f in text.vocab().most_common(selected_words_num)]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]
    
# SPM Tokenizer
train_x = [term_frequency(d) for d, _ in train_docs_spm]
test_x = [term_frequency(d) for d, _ in test_docs_spm]
train_y = [c for _, c in train_docs_spm]
test_y = [c for _, c in test_docs_spm]

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
    token = spm_tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
    score = float(model.predict(data))
    with open(str(selected_words_num)+'_'+str(epoch)+'_SPM_'+chatlogFileName, 'a', encoding='utf-8') as f:
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