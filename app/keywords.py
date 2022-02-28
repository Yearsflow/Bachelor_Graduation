from keybert import KeyBERT
import spacy
import jieba

def extract_keywords_model():
    zh_model=spacy.load('zh_core_web_sm')
    model=KeyBERT(model=zh_model)
    return model