import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,recall_score,f1_score

def transform_label(df):
    label={'history':0,'military':1,'baby':2,'world':3,'tech':4,
        'game':5,'society':6,'sports':7,'travel':8,'car':9,
        'food':10,'entertainment':11,'finance':12,'fashion':13,
        'discovery':14,'story':15,'regimen':16,'essay':17}
    for i in range(len(df)):
        df['label'][i]=label[df['label'][i]]
    return df

def evaluate(result,test_Y):
    print('Accuracy:',accuracy_score(test_Y,result))
    print('Recall:',recall_score(test_Y,result,average='macro'))
    print('F1:',f1_score(test_Y,result,average='macro'))

def TP_MLmodels(classifier,train_X,train_Y,test_X,test_Y,classifier_name):
    classifier.fit(train_X,train_Y)
    result=classifier.predict(test_X)
    print(classifier_name+':')  
    evaluate(result,test_Y)
    return classifier,result