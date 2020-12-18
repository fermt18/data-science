# data exists in two separate sources
import numpy as np
import pandas as pd

# concatenation: when both sources are in the same format
data_one = {'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']}
data_two = {'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}
one = pd.DataFrame(data_one)
two = pd.DataFrame(data_two)
print(pd.concat([one,two], axis=1)) # concatenate along columns
print(pd.concat([one,two], axis=0)) # concatenate along rows, NaN where colun has no value
two.columns = one.columns
mydf = pd.concat([one,two], axis=0)
print(mydf) # concatenate along rows, column C,D relabel by columns A,B but index is repeated
mydf.index = range(len(mydf))
print(mydf) # index reset

# merge: when both sources are not in the exact same order or format (analogous to JOIN in SQL)
# inner merge: gets data present in both tables
registrations = pd.DataFrame({'reg_id':[1,2,3,4], 'name':['Andrew', 'Bobo', 'Claire', 'David']})
logins = pd.DataFrame({'log_id':[1,2,3,4], 'name':['Xavier', 'Andrew','Yolanda','Bobo']})
print(pd.merge(registrations, logins, how='inner', on='name')) # inner join: name matching in both tables, order of tables passed does not matter

# left, right merge: gets all data from one table and what matches from the second table
print(pd.merge(registrations, logins, how='left', on='name')) # left join: all registrations + matching logins, order of tables passed matters
print(pd.merge(registrations, logins, how='right', on='name')) # right join: all logins + matching registrations, order of tables passed matters

# outer merge: gets all data from both tables
print(pd.merge(registrations, logins, how='outer', on='name')) # outer join: name present in both tables, order of tables passed does not matter


registrations = registrations.set_index('name')
pd.merge(registrations, logins, left_index=True, right_on='name', how='inner') # same as inner merge