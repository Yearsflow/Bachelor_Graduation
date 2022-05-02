import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from snownlp import SnowNLP
import joblib
import numpy as np

file1='./train_text_data/中文停用词表.txt'
file2='./train_text_data/哈工大停用词表.txt'
file3='./train_text_data/四川大学机器智能实验室停用词库.txt'
label_df={'history':0,'military':1,'baby':2,'world':3,'tech':4,
        'game':5,'society':6,'sports':7,'travel':8,'car':9,
        'food':10,'entertainment':11,'finance':12,'fashion':13,
        'discovery':14,'story':15,'regimen':16,'essay':17}
stopwords_set=set()
with open(file1,'r',encoding='utf-8') as f1,\
    open(file2,'r',encoding='utf-8') as f2,\
    open(file3,'r',encoding='utf-8') as f3:
    for word in f1.readlines():
        stopwords_set.add(word.strip())
    for word in f2.readlines():
        stopwords_set.add(word.strip())
    for word in f3.readlines():
        stopwords_set.add(word.strip())

def tokenize(text):
    model = SnowNLP(text)
    text_token = model.words
    result = ''
    for word in text_token:
        result += word + ' '
    return result.strip(' ')

def save_Chinese_contents(text):
    words = text.split(' ')
    result = ''
    for word in words:
        if word >= u'\u4e00' and word <= u'\u9fa5':
            result += word + ' '
    return result

def remove_stopwords(text):
    words = text.split(' ')
    result = ''
    for word in words:
        if word not in stopwords_set:
            result += word + ' '
    return result

def clean(text):
    text = tokenize(text)
    text = save_Chinese_contents(text)
    text = remove_stopwords(text)
    return text

def vectorize(text):
    text = clean(text)
    vectorizer = joblib.load('./model/CountVectorizer.pkl')
    transformer = joblib.load('./model/TfidfTransformer.pkl')
    tfidf = transformer.transform(vectorizer.transform([text]))
    return tfidf

def label2id(label):
    return label_df[label]

def id2label(Id):
    return list(label_df.keys())[list(label_df.values()).index(Id)]

def predict_label(model_name, text):
    model = joblib.load('./model/' + model_name + '.pkl')
    matrix = vectorize(text)
    res = model.predict(matrix)
    return id2label(res[0])

def keywords(text, num=3):
    model = SnowNLP(text)
    return model.keywords(num)
