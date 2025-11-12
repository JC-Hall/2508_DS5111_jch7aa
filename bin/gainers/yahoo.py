from bin.gainers.base import GainerBase
import os
import pandas as pd

class GainerYahoo(GainerBase):
    def __init__(self):
        pass

    def download_html(self):
        print("yahoo html download")
        os.system("sudo google-chrome-stable --headless --disable-gpu --dump-dom --lang=en-US --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html")

    def extract_csv(self):
        print("yahoo csv create")
        raw = pd.read_html('ygainers.html')
        raw[0].to_csv('ygainers.csv')

    def normalize_data(self, filepath='ygainers.csv'):
        print("yahoo normalize csv")
        df = pd.read_csv(filepath)
        df['symbol'] = df['Symbol']
        df['company_name'] = df['Name']
        df['price'] = df['Price'].astype(str).apply(lambda x: str(x).split()[0])
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df['change'] = df['Change']
        df['perc_change'] = (df['Change %'].astype(str)
                .str.replace('%', '', regex=False)
                .str.replace('+', '', regex=False)
        )
        df['volume'] = df['Volume']

        final = df[['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']].dropna()
        final.to_csv('normalized_yahoo.csv', index=False)
        print(final)

if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Please pass in one of 'html', 'csv', 'normalize'"
    function = sys.argv[1]
    valid_functions = ['html', 'csv', 'normalize']
    assert function in valid_functions, f"Expected one of {valid_functions} but got {function}"

    gainer = GainerYahoo()

    if function == 'html':
        gainer.download_html()
    elif function == 'csv':
        gainer.extract_csv()
    elif function == 'normalize':
        gainer.normalize_data()
