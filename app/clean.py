import jieba

def get_stopwords():
    file1='./data/中文停用词表.txt'
    file2='./data/哈工大停用词表.txt'
    file3='./data/四川大学机器智能实验室停用词库.txt'
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
    return stopwords_set

def split_words(text):
    stopwords=get_stopwords()
    words=jieba.cut(text)
    txt=''
    for word in words:
        if word not in stopwords:
            txt+=word+' '
    return txt

def extract_Chinese(text):
    words=text.split(' ')
    txt=''
    for word in words:
        if word>=u'\u4e00' and word<=u'\u9fa5':
            txt+=word+' '
    return txt

def clean_text(text):
    text=extract_Chinese(text)
    text=split_words(text)
    return text