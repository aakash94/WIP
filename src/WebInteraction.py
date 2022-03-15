import pandas as pd
import lyricsgenius as lg  # pip install git+https://github.com/johnwmillr/LyricsGenius.git
import os


class WebInteraction():

    def __init__(self):
        token = ""
        token_path = os.path.join("..", "res", "GeniusToken")
        with open(token_path) as f:
            token = f.readlines()[0]
        self.genius = lg.Genius(token,
                                skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                                remove_section_headers=True)

    def get_dataframe_from_url(self, url_link):
        try:
            df = pd.read_html(url_link)
            return df
        except:
            return []

    def lyrics_things(self, song_name, artist):

        lyrics = []

        try:
            songs = self.genius.search_song(artist, song_name)
            lyrics = songs.lyrics  # search for song in songs, lyrics as string
            lyrics = lyrics.split('\n', 1)[1]  # removing the head

        except:
            print(f"could not find lyrics to  {song_name}")

        return lyrics


if __name__ == '__main__':
    wi = WebInteraction()
    url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Record_of_the_Year"
    df = wi.get_dataframe_from_url(url_link=url)
    print(df)
