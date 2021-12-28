# clean or manipulate text data
import numpy as np
import pandas as pd

names = pd.Series(['andrew', 'bobo', 'claire', 'david', '5'])
names.str.upper() # methods apply to all strings in the series
'5'.isdigit() # True
print(names.str.isdigit())

tech_finance = ['GOOG,APPL,AMZN', 'JPM,BAC,GS']
tickers = pd.Series(tech_finance)
tickers.str.split(',')[0] # first item
tickers.str.split(',').str[0] # first item from the two groups
print(tickers.str.split(',', expand=True)) # splits and returns a DataFrame

messy_names = pd.Series(['andrew ', 'bo;bo', '   claire   '])
print(messy_names
    .str.replace(';', '')
    .str.strip()
    .str.capitalize())