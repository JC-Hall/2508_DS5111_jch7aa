from bin.gainers.base import GainerBase
import os
import re
import pandas as pd


class GainerWSJ(GainerBase):
    def __init__(self):
        pass

    def download_html(self):
        print("wsj html download")
        os.system("sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 https://www.wsj.com/market-data/stocks/us/movers > wsjgainers.html")

    def extract_csv(self):
        print("wsj csv create")
        raw = pd.read_html('wsjgainers.html')
        raw[0].to_csv('wsjgainers.csv')

    def normalize_data(self, filepath='wsjgainers.csv'):
        print("wsj normalize csv")
        df = pd.read_csv(filepath)
        rex = r'\(([A-Z]+)\)$'
        df['symbol'] = df['Unnamed: 0'].astype(str).apply(lambda x: re.findall(rex, x)[0])
        df['company_name'] = df['Unnamed: 0'].astype(str).apply(lambda x: re.findall(rex, x)[0])
        df['price'] = df['Last']
        df['change'] = df['Chg']
        df['perc_change'] = df['% Chg']
        df['volume'] = df['Volume']

        final = df[['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']].dropna()
        final.to_csv('normalized_wsj.csv', index=False)
        print(final)


if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Please pass in one of 'html', 'csv', 'normalize'"
    function = sys.argv[1]
    valid_functions = ['html', 'csv', 'normalize']
    assert function in valid_functions, f"Expected one of {valid_functions} but got {function}"

    gainer = GainerWSJ()

    if function == 'html':
        gainer.download_html()
    elif function == 'csv':
        gainer.extract_csv()
    elif function == 'normalize':
        gainer.normalize_data()
