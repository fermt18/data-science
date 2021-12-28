# allows you to reorganize data, refactoring cells based on columns and a new index
import pandas as pd
import numpy as np

df = pd.read_csv('auxfiles/Sales_Funnel_CRM.csv')
print(df)

# how many licenses of each product did google purchased?
licenses = df[['Company', 'Product', 'Licenses']]
print(pd.pivot(data=licenses, index='Company', columns='Product', values='Licenses'))

# how much is sold by company?
print(pd.pivot_table(df, index='Company', aggfunc='sum'))
df.groupby('Company').sum() # same with groupby

# licenses for account manager and contacts?
print(pd.pivot_table(df, index=['Account Manager', 'Contact'], values=['Sale Price'], aggfunc='sum'))
print(pd.pivot_table(df, index=['Account Manager', 'Contact'], values=['Sale Price'], columns=['Product'], aggfunc=np.sum, fill_value=0))