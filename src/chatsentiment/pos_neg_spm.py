import json
import nltk
import numpy as np
from tensorflow.keras import models
from tensorflow.keras.models import load_model
import sentencepiece as spm

def predict_pos_neg(review):
    if 'session' in locals() and session is not None:
        session.close()
        
    with open('../chatsentiment/train_docs_spm.json', encoding='utf-8') as f:
        train_docs_spm = json.load(f)
    model = load_model('../chatsentiment/posneg_model.h5')

    tokens = [t for d in train_docs_spm for t in d[0]]

    text = nltk.Text(tokens, name='NMSC')
    selected_words = [f[0] for f in text.vocab().most_common(5000)]

    sp=spm.SentencePieceProcessor()
    sp.Load('../chatsentiment/spm_tokenizer.model')
    rst=[]
    for line in review:
        token = sp.EncodeAsPieces(line)
        tf=[]
        for word in selected_words:
            tf.append(token.count(word))
        
        data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
        score = float(model.predict(data))
        if(score > 0.2):
            rst.append(1)
        else:
            rst.append(0)
    return rst