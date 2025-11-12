from bin.gainers.base import GainerBase
import os
import re
import pandas as pd


class GainerCNBC(GainerBase):
    def __init__(self):
        pass

    def download_html(self):
        print("cnbc html download")
        #os.system("sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 https://www.cnbc.com/nasdaq-100/ > cnbcgainers.html")

    def extract_csv(self):
        print("cnbc csv create")
        #raw = pd.read_html('cnbcgainers.html')
        #raw[0].to_csv('cnbcgainers.csv')

    def normalize_data(self, filepath='cnbcgainers.csv'):
        print("cnbc normalize csv")
	#df = pd.read_csv(filepath)
        #df['symbol'] = df['SYMBOL']
        #df['name'] = df['NAME']
        #df['price'] = df['Price'].astype(str).apply(lambda x: str(x).split()[0])
        #df['price'] = pd.to_numeric(df['price'], errors='coerce')
        #df['change'] = df['change']
        #df['perc_change'] = df['%change']

        #final = df[['symbol', 'company_name', 'price', 'change', 'perc_change']].dropna()
        #final.to_csv('normalized_cnbc.csv', index=False)
        #print(final)


if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Please pass in one of 'html', 'csv', 'normalize'"
    function = sys.argv[1]
    valid_functions = ['html', 'csv', 'normalize']
    assert function in valid_functions, f"Expected one of {valid_functions} but got {function}"

    gainer = GainerCNBC()

    if function == 'html':
        gainer.download_html()
    elif function == 'csv':
        gainer.extract_csv()
    elif function == 'normalize':
        gainer.normalize_data()
