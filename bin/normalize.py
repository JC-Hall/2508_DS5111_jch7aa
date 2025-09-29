"""Data normalization script for Yahoo and WSJ CSV files."""

import re
import sys
import pandas as pd


def normalize_y(filepath):
    """Normalize Yahoo CSV data"""
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

def normalize_wsj(filepath):
    """Normalize WSJ CSV data"""
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


if __name__ == '__main__':
    filepath = sys.argv[1]

    if filepath.startswith('y'):
        normalize_y(filepath)
    else:
        normalize_wsj(filepath)
