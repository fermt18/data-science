# table of colums and rows that we can restructure
# set of Pandas Series objects that share the same index
import numpy as np
import pandas as pd

np.random.seed(101)
mydata = np.random.randint(0, 101, (4,3))
myindex = ['CA', 'NY', 'AZ', 'TX']
mycols  = ['Jan', 'Feb', 'Mar']
df = pd.DataFrame(mydata)
print(df)
df = pd.DataFrame(mydata, myindex, mycols)
print(df)
df.info()

df = pd.read_csv('auxfiles/tips.csv')
print(df)

df.columns # list of column names as strings
df.index # index range
df.head(10) # firts 10 rows
df.tail() # last 5 rows
df.describe() # descriptive statistics
df.describe().transpose()

df['total_bill'] # series with total_bill column values
mycols = ['total_bill', 'tip']
df[mycols] # dataframe with the two columns values
df['tip'] + df['total_bill'] # sums every single row
df['tip_percent'] = 100 * df['tip'] / df['total_bill'] # percentage of tip against total bill in a new column
df['price_per_person'] = np.round(df['total_bill'] / df['size'], 2)
print(df.head())

df = df.drop('tip_percent', axis=1) # remove the column

df = df.set_index('Payment ID') # unique column value as index instead of the numeric index - num nidex not working
print(df.head)
df = df.reset_index() # back to numeric index

df.iloc[0] # series with the row with index 0
df.loc['Sun2959'] # series with the row with index as string
df.loc[['Sun2959'], ['Sum2222']] # dataframe with the two rows with index as string

df = df.drop('Sun2959', axis = 0) # remove the row
df = df.append(one_row)