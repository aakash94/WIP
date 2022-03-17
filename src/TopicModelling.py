# data visualisation and manipulation
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
import sklearn
from sklearn.decomposition import LatentDirichletAllocation

#configure
# sets matplotlib to inline and displays graphs below the corressponding cell.
#%matplotlib inline
style.use('fivethirtyeight')
sns.set(style='whitegrid',color_codes=True)

#import nltk
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize

#preprocessing
from nltk.corpus import stopwords  #stopwords
from nltk import word_tokenize,sent_tokenize # tokenizing
from nltk.stem import PorterStemmer,LancasterStemmer  # using the Porter Stemmer and Lancaster Stemmer and others
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer  # lammatizer from WordNet

# for named entity recognition (NER)
from nltk import ne_chunk

# vectorizers for creating the document-term-matrix (DTM)
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer

#stop-words
stop_words=set(nltk.corpus.stopwords.words('english'))

class TopicModelling():

    def __init__(self):
        self.tm = TopicModelling()
        self.res_path = os.path.join("..", "res", )

    def clean_text(self, text_str):   #df['texts_want_clean']=df['texts_want'].apply(clean_text)
        le = WordNetLemmatizer()
        word_tokens = word_tokenize(text_str)
        tokens = [le.lemmatize(w) for w in word_tokens if w not in stop_words and len(w) > 3]
        cleaned_text = " ".join(tokens)
        return cleaned_text

    def make_corpus(self, df, column):
        clean_corpus = []
        for column in df:
            clean_corpus.append(self.clean_text(df[column]).split())
        return clean_corpus



