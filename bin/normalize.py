import pandas as pd
import numpy as np
import re
import sys


def normalize_y(fname):
	df = pd.read_csv(fname)
	df['symbol'] = df['Symbol']
	df['company_name'] = df['Name']
	df['price'] = df['Price'].astype(str).apply(lambda x: str(x).split()[0])
	df['price'] = pd.to_numeric(df['price'], errors='coerce')
	df['change'] = df['Change']
	df['perc_change'] = df['Change %'].astype(str).str.replace('%', '', regex=False).str.replace('+', '', regex=False)
	df['volume'] = df['Volume']

	final = df[['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']].dropna()
	print(final)

def normalize_wsj(fname):
	df = pd.read_csv(fname)
	rex = r'\(([A-Z]+)\)$'
	df['symbol'] = df['Unnamed: 0'].astype(str).apply(lambda x: re.findall(rex, x)[0])
	df['company_name'] = df['Unnamed: 0'].astype(str).apply(lambda x: re.findall(rex, x)[0])
	df['price'] = df['Last']
	df['change'] = df['Chg']
	df['perc_change'] = df['% Chg']
	df['volume'] = df['Volume']

	final = df[['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']].dropna()
	print(final)	


if __name__ == '__main__':
	fname = sys.argv[1]

	if fname.startswith('y'):
		normalize_y(fname)
	else:
		normalize_wsj(fname)
