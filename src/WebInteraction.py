import pandas as pd
import lyricsgenius as lg #pip install git+https://github.com/johnwmillr/LyricsGenius.git


class WebInteraction():

    def __init__(self):
        genius = lg.Genius('tbQ-t4_zZ6HU1JfmDnrhx30Dve1abSJ-FUq3WJIaflHDhUppnMRV4meiFI8Vob6o',
                           skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                           remove_section_headers=True)

    def get_dataframe_from_url(self, url_link):
        df = pd.read_html(url_link)
        return df

    def lyrics_things(self, song_name, artist):

        lyrics = []

        try:
            songs = genius.search_artist(artist,max_songs = 10, include_features=True) #top 10 songs of artics
            lyrics = songs.song(song_name).lyrics #search for song in songs, lyrics as string
            lyrics = lyrics.split('\n',1)[1] #removing the head

        except:
            print('sorry, could not find songzzzz')

        return lyrics


if __name__ == '__main__':
    wi = WebInteraction()
    url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Record_of_the_Year"
    df = wi.get_dataframe_from_url(url_link=url)
    print(df)
