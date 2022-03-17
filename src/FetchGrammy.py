import pandas as pd
import numpy as np
import os
import re
from tqdm import tqdm
from WebInteraction import WebInteraction

YEAR_STRING = 'Year[I]'
RECORD_STRING = 'Record'
ARTISTS_STRING = 'Artist(s)'

DATAFRAME_HEADER = ['year', 'record', 'artist', 'gender', 'lyrics', 'sentiment']
DELIMITER = "\t"


class FetchGrammy():

    def __init__(self):
        self.wi = WebInteraction()
        self.res_path = os.path.join("..", "res", )

    def get_artist_gender(self, artist_name: str):
        artist_name = artist_name.strip()
        artist_name = artist_name.replace(' ', '+')
        gender = 'Unknown'
        mb_url = "https://musicbrainz.org/search?query=" + artist_name + "&type=artist&limit=1"
        dfs = self.wi.get_dataframe_from_url(url_link=mb_url)
        if len(dfs) > 0:
            df = dfs[0]  # since only 1 row queried
            gender = df['Gender'][0]
            if isinstance(gender, np.floating):
                # gender is empty in the site
                gender = 'Unknown'
        return gender

    def get_artist_age(self, artist_name):
        # TODO : Get age of artists here
        ...

    def get_album_from_song(self, song_name, artist_name):
        # TODO : Get song name
        ...

    def get_genre_from_album(self, album_name):
        # TODO : Get genre of an album
        ...

    def get_commentary_(self):
        # TODO : Decide on what's available and fetch it
        ...

    def get_nytimes_(self):
        # TODO : Decide on what's available and fetch it
        ...

    def get_lyrics(self, song_name, artist):
        # file = open("/Users/User/Desktop/auto_.txt", "w")
        pattern = r'[0-9]'
        lyrics = self.wi.lyrics_things(song_name=song_name, artist=artist)
        length = len(lyrics) - len("Embed")
        if length > 0:
            # there is some lyrics, and it is not just plain empty string
            lyrics = lyrics[:length]
            lyrics = re.sub(pattern, '', lyrics)
            # remove all occurrences of the delimiter from the lyrics
            lyrics = re.sub(DELIMITER, '', lyrics)
        return lyrics

    def get_record_of_the_year(self):
        records = []
        url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Record_of_the_Year"
        tables = self.wi.get_dataframe_from_url(url_link=url)
        del tables[0]  # remove the header table
        del tables[0]  # remove 1959
        tables = tables[:-3]  # remove tables at the end

        df = pd.DataFrame()
        for t in tqdm(tables):
            # try:
            df = t[[YEAR_STRING, RECORD_STRING, ARTISTS_STRING]]
            for index, row in df.iterrows():
                year = row[0]
                year = year[0: 4]
                print(year)
                record = row[1]
                artists = row[2]
                lyrics = self.get_lyrics(song_name=record, artist=artists)
                gender = self.get_artist_gender(artist_name=artists)
                song_info = (year, record, artists, gender, lyrics)
                records.append(song_info)
            # except Exception as e:
            # print(e)
        df = pd.DataFrame(records, columns=DATAFRAME_HEADER)
        return df

    def save_pkl(self, dataframe: pd.DataFrame, file_name="fg.pkl"):
        # motivation: automatically saves dfs in the res folder,
        # and unless required the file name need not be mentioned everytime
        path = os.path.join(self.res_path, file_name)
        dataframe.to_pickle(path)

    def save_tsv(self, dataframe: pd.DataFrame, file_name="fg.tsv"):
        # motivation: automatically saves dfs in the res folder,
        # and unless required the file name need not be mentioned everytime
        path = os.path.join(self.res_path, file_name)
        dataframe.to_csv(path, sep=DELIMITER, index=False)

    def load_pkl(self, file_name="fg.pkl"):
        # motivation: automatically loads df from the res folder,
        # and unless required the file name need not be mentioned everytime
        path = os.path.join(self.res_path, file_name)
        dataframe = pd.read_pickle(path)
        return dataframe

    def load_tsv(self, file_name="fg.tsv"):
        # motivation: automatically loads df from the res folder,
        # and unless required the file name need not be mentioned everytime
        path = os.path.join(self.res_path, file_name)
        dataframe = pd.read_csv(path, sep=DELIMITER)
        return dataframe


if __name__ == '__main__':
    fg = FetchGrammy()
    # records = fg.get_record_of_the_year()
    # fg.save_pkl(dataframe=records)
    records = fg.load_tsv()
    '''
    # records['gender'] = records.apply(lambda row: fg.get_artist_gender(artist_name=row['artist']), axis=1)
    records['lyrics'] = records.apply(lambda row: fg.get_lyrics(song_name=row['record'], artist=row['artist']), axis=1)
    print(records)
    fg.save_tsv(dataframe=records)    
    
    for ind in records.index:
        print("\n\n\n----------------")
        for i in DATAFRAME_HEADER:
            print(records[i][ind])
    '''
