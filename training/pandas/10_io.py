# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
import pandas as pd

# csv
import os
print(os.getcwd()) # get current working directory
df = pd.read_csv('auxfiles/example.csv', index_col=0) # 0 index col as index
df.to_csv('ex.csv', index=False) # saves in cwd and with default index


# html
# pandas can convert table html tag into a dataframe
url = "https://en.wikipedia.org/wiki/World_population"
tables = pd.read_html(url) # try to get every single table from the html doc; also works from local html file
print(len(tables))
top_ten = tables[1] # multi livel index table
top_ten = top_ten['World population (millions, UN estimates)[14]']
top_ten = top_ten.drop(11, axis=0) # dropping notes line
top_ten = top_ten.drop('#', axis=1) # drop index column
print(top_ten)
top_ten.to_html('ex.html', index=False)


# excel
# only to abole ot read raw data not formulas, macro code, ...
df = pd.read_excel('auxfiles/my_excel_file.xlsx', sheet_name='First_Sheet', engine='openpyxl')
print(df)
wd_dict = pd.read_excel('auxfiles/my_excel_file.xlsx', sheet_name=None, engine='openpyxl') # read everything, creates dictionary
print(wd_dict.keys()) # keys are sheets, values are DF
my_df = wd_dict['First_Sheet']
my_df.to_excel('ex.xlsx', sheet_name='First_Sheet', index=False)


# sql
# based on python drivers depending on teh sql engine
# https://docs.sqlalchemy.org/en/13/dialects/index.html
from sqlalchemy import create_engine
import numpy as np

temp_db = create_engine('sqlite:///:memory:')
df = pd.DataFrame(data=np.random.randint(low=0, high=100, size=(4,4)), columns=['a','b','c','d'])
df.to_sql(name='new_table', con=temp_db)
new_df = pd.read_sql(sql='new_table', con=temp_db) # read entire table (for small tables)
print(new_df)
print(pd.read_sql_query(sql='SELECT a,c FROM new_table', con=temp_db))
