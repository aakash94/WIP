import pandas as pd

from WebInteraction import WebInteraction

YEAR_STRING = 'Year[I]'
RECORD_STRING = 'Record'
ARTISTS_STRING = 'Artist(s)'

DATAFRAME_HEADER = ['year', 'record', 'artist', 'lyrics']


class FetchGrammy():

    def __init__(self):
        self.wi = WebInteraction()

    def get_lyrics(self, song_name, artist):
        lyrics = ''
        return lyrics

    def get_record_of_the_year(self):
        records = []
        url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Record_of_the_Year"
        tables = self.wi.get_dataframe_from_url(url_link=url)
        del tables[0]  # remove the header table
        del tables[0]  # remove 1959

        for t in tables:
            df = pd.DataFrame()
            try:
                df = t[[YEAR_STRING, RECORD_STRING, ARTISTS_STRING]]
                for index, row in df.iterrows():
                    year = row[0]
                    year = year[0: 4]
                    record = row[1]
                    artists = row[2]
                    lyrics = self.get_lyrics(song_name=record, artist=artists)
                    song_info = (year, record, artists, lyrics)
                    records.append(song_info)
            except:
                ...
            df = pd.DataFrame(records, columns=DATAFRAME_HEADER)
        return df



if __name__ == '__main__':
    fg = FetchGrammy()
    records = fg.get_record_of_the_year()

    for ind in records.index:
        print("----------------")
        for i in DATAFRAME_HEADER:
         print(records[i][ind])