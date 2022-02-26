import pandas as pd


class WebInteraction():

    def __init__(self):
        '''
        Use this class to write all web interaction related calls.
        '''
        pass

    def get_dataframe_from_url(self, url_link):
        df = pd.read_html(url_link)
        return df


if __name__ == '__main__':
    wi = WebInteraction()
    url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Record_of_the_Year"
    df = wi.get_dataframe_from_url(url_link=url)
    print(df)
