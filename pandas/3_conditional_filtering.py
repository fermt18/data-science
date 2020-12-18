# for large datasets, data is filtered on conditions instead of indexes
# columns are features
import numpy as np
import pandas as pd

df = pd.read_csv('auxfiles/tips.csv')

bool_series = df['total_bill'] > 40 # returns boolean series according to the condition
df[bool_series] # returns df with rows fulfilling the condition

print(df[(df['total_bill'] > 30) & (df['sex'] == "Male")]) # AND operation ('and' won't work)

options = ['Sat', 'Sun']
print(df['day'].isin(options)) # instead of chaining OR conditions