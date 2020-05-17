# -*- coding: utf-8 -*-
import codecs

from konlpy.tag import Okt
okt = Okt()

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import time
import joblib
import pickle

def fitting(sample_labels, sample_text):
	test_start = int(len(sample_text)/5)*4
	test_end = len(sample_text)
	
	test_text = sample_text[test_start:test_end]
	test_labels = sample_labels[test_start:test_end]
	train_text = sample_text[:test_start]
	train_labels = sample_labels[:test_start]

	test_text_ = [' '.join(word[0] for word in okt.pos(text, norm=True)) for text in test_text]

	trained_vectorizer = TfidfVectorizer(ngram_range=(1, 1))
	train_text_feat = trained_vectorizer.fit_transform(train_text)
	test_text_feat = trained_vectorizer.transform(test_text_)

	pickle.dump(trained_vectorizer, open("vectorizer.pickle", "wb"))

	trained_clf = svm.SVC(kernel='linear').fit(train_text_feat, train_labels)
	trained_clf.fit(train_text_feat, train_labels)

	joblib.dump(trained_clf, '7sentiment.model') 

	predicted = trained_clf.predict(test_text_feat)

	j = 0; correct = 0.0
	for label in test_labels:
		if predicted[j] == label:
			correct = correct + 1
		j = j + 1
	acc = correct / j

	return acc

def predict(chat):
	vectorizer = pickle.load(open("vectorizer.pickle", "rb"))
	chat_feat = vectorizer.transform(chat)
	model = joblib.load('7sentiment.model')
	return model.predict(chat_feat)

def counting(a):
	sentiment = ['joy', 'sadness', 'neutral', 'fear', 'love', 'surprise', 'anger']
	dic = {}
	for s in sentiment:
		dic[s] = a.count(s)
	return dic

sample_text = []; sample_labels = []
for line in codecs.open('./data/chat_data.tsv', 'r', 'utf-8'):
	label, text = line.strip().split('\t')
	text = ' '.join(word[0] for word in okt.pos(text, norm=True))

	sample_text.append(text)
	sample_labels.append(label)

print(len(predict(sample_text)))