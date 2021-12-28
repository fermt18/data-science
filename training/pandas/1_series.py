# https://pandas.pydata.org/docs
# series: one-dimensional ndarray with axis labes
# this is like a NumPy array with a non-numeric index, but still numerically organized
import numpy as np
import pandas as pd

myIndex = ['USA', 'Canada', 'Mexico']
myData =  [1776, 1867, 1821]
mySeries = pd.Series(data = myData)
mySeries = pd.Series(data = myData, index=myIndex)
print(mySeries)

ages = {'Sam':5, 'Frank':10, 'Spike':7}
print(pd.Series(ages))

# Sales data for 1st and 2nd Quarters for Global Company
q1 = {'Japan':80, 'China':450, 'India':200, 'USA':250}
q2 = {'Brazil':100, 'China':500, 'India':210, 'USA':260}
sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)
sales_q1['Japan']
sales_q1[0]
sales_q1.keys()
sales_q1 * 2 # broadcast operation to all elements

print(sales_q1 + sales_q2) # operations with different indexes are added as long as the index exists in both
print(sales_q1.add(sales_q2, fill_value = 0)) # fil non matching indexes with a 0 (so +0 when added)
