from FetchGrammy import FetchGrammy
from TFIDF import TFIDF

def main():
    print("Hello World!\nWelcome to WIP Project")
    fg = FetchGrammy()
    #l = fg.get_lyrics(song_name="Kiss me more", artist="Doja Cat")
    #print(l)
    records = fg.load_tsv()
    print(len(records))
    tfidf = TFIDF()
    # tfidf.create_corpus(dataframe=records)
    # x = tfidf.tfidf_vectorize(dataframe=records)
    # print(x.shape)
    # tfidf.show_elbow(t_vector=x)
    # elbow looks to be at 5
    tfidf.k_means(dataframe=records)


if __name__ == '__main__':
    main()
