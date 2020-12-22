import numpy as np
import pandas as pd

from datetime import datetime

myyear = 2015
mymonth = 1
myday = 1
myhour = 2
mymin = 30
mysec = 15
mydate = datetime(myyear, mymonth, myday, myhour, mymin)

myser = pd.Series(['Nov 3, 1990', '2000-01-01', None])
print(pd.to_datetime(myser))

euro_date = '10-12-2000'
pd.to_datetime(euro_date, dayfirst=True)

sales = pd.read_csv('auxfiles/RetailSales_BeerWineLiquor.csv')
print(sales) # date column is an object
sales['DATE'] = pd.to_datetime(sales['DATE'])
print(sales)
sales['DATE'][0].year

sales = pd.read_csv('auxfiles/RetailSales_BeerWineLiquor.csv', parse_dates=[0]) #first column is date
sales['DATE'].dt.year

sales.resample(rule='A').mean() # offser alias (A: year and frequency, check docu)
