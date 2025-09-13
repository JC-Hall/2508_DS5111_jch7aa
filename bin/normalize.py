import pandas as pd
import numpy as np
import re

def normalize_y():
	df = pd.read_csv('ygainers.csv')
	df['entry_price'] = df['Price'].astype(str).apply(lambda x: str(x).split()[0])
	df['entry_price'] = pd.to_numeric(df['entry_price'], errors='coerce')
	print(df[['Price', 'entry_price']].head())

def normalize_wsj():
	df = pd.read_csv('wsjgainers.csv')
	rex = r'\(([A-Z]+)\)$'
	df['sym'] = df['Unnamed: 0'].astype(str).apply(lambda x: re.findall(rex, x)[0])
	print(df[['Unnamed: 0', 'sym']].head())

if __name__ == '__main__':
	normalize_y()
	normalize_wsj()
