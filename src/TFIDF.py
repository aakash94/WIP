from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from wordcloud import WordCloud
import pandas as pd
import nltk
import os


class TFIDF():

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        # no need to do this everytime it's needed to clean something
        self.words = set(nltk.corpus.words.words())

    def create_corpus(self, dataframe: pd.DataFrame):
        lyrics = dataframe['lyrics']
        all_lyrics = list(dataframe['lyrics'].values[1:])
        clean_lyrics = []
        for l in all_lyrics:
            clean = self.clean_string(text=l)
            clean_lyrics.append(clean)
        return clean_lyrics

    def clean_string(self, text: str):
        # https: // stackoverflow.com / a / 41290205
        # use this to 'clean' lyrics in whatever way seen fit
        clean_text = ""
        clean_text = " ".join(w for w in nltk.wordpunct_tokenize(text) if w.lower() in self.words or not w.isalpha())
        # can add more steps down here
        return clean_text

    def tfidf_vectorize(self, dataframe: pd.DataFrame):
        lyrics = self.create_corpus(dataframe=dataframe)
        vectorizer = TfidfVectorizer(stop_words={'english'})
        t_vector = vectorizer.fit_transform(lyrics)
        # print(vectorizer.get_feature_names_out()) # list of all words
        # print(len(vectorizer.get_feature_names_out())) # length of above words
        # t_vector is a matrix, 1 row for each row in dataframe and width same as the length of words
        return t_vector, lyrics

    def show_elbow(self, t_vector):
        # https://towardsdatascience.com/clustering-documents-with-python-97314ad6a78d
        Sum_of_squared_distances = []
        K = range(2, 10)
        for k in K:
            km = KMeans(n_clusters=k, max_iter=200, n_init=10)
            km = km.fit(t_vector)
            Sum_of_squared_distances.append(km.inertia_)
        plt.plot(K, Sum_of_squared_distances, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Sum_of_squared_distances')
        plt.title('Elbow Method For Optimal k')
        plt.show()

    def k_means(self, dataframe: pd.DataFrame, k=5):
        t_vector, lyrics = self.tfidf_vectorize(dataframe=dataframe)
        song_titles = dataframe['record'].tolist()
        model = KMeans(n_clusters=k, init='k-means++', max_iter=200, n_init=10)
        model.fit(t_vector)
        labels = model.labels_
        lyrics_cluster = pd.DataFrame(list(zip(song_titles, labels)), columns=['title', 'cluster'])
        print(lyrics_cluster.sort_values(by=['cluster']))
        self.show_wordcloud(labels=labels, lyrics=lyrics, cluster=lyrics_cluster, k=k)

    def show_wordcloud(self, labels, lyrics, cluster, k=5):
        result = {'cluster': labels, 'lyrics': lyrics}
        result = pd.DataFrame(result)
        for k in range(0, k):
            s = result[result.cluster == k]
            text = s['lyrics'].str.cat(sep=' ')
            text = text.lower()
            text = ' '.join([word for word in text.split()])
            wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
            print('Cluster: {}'.format(k))
            print('Titles')
            titles = cluster[cluster.cluster == k]['title']
            print(titles.to_string(index=False))
            plt.figure()
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.show()

    if __name__ == '__main__':
        pass
