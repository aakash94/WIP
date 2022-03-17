from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import download

class SentimentAnalysis():

    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def get_score(self, lyrics):
        # 1 = Positive
        # 0 = Neutral
        # -1 = Negative
        # Values are continuous in the range -1 1
        comp = self.sid.polarity_scores(lyrics)
        print(comp)
        comp = comp['compound']
        return comp

    def get_sentiment(self, lyrics):
        score = self.get_score(lyrics=lyrics)
        if score >= 0.5:
            return 1
        elif score > -0.5 and score < 0.5:
            return 0
        else:
            return -1


if __name__ == '__main__':
    # run once
    # download('vader_lexicon')
    sa = SentimentAnalysis()
    lyrics = """I wanna die."""

    s = sa.get_sentiment(lyrics=lyrics)
    print(s)
