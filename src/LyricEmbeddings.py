import os

class LyricEmbeddings():

    def __init__(self):
        pass

    def get_embeddings(self, lyrics):
        embeddings = None
        return embeddings

    def get_embedding_similarity(self, embedding1, embedding2):
        similarity = None
        return similarity

    def get_lyric_similarity(self, lyric1, lyric2):
        embedding1 = self.get_embeddings(lyrics=lyric1)
        embedding2 = self.get_embeddings(lyrics=lyric2)
        similarity = self.get_embedding_similarity(self, embedding1, embedding2)
        return


if __name__ == '__main__':
    le = LyricEmbeddings()
    lyrics1 = ""
    lyrics2 = ""
    le.get_lyric_similarity(lyric1=lyrics1, lyric2=lyrics2)
