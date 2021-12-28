
import pandas as pd
import numpy as np

def last_four_digits(num):
    return str(num)[-4:]

def yelp(price):
    if price < 10:
        return '$'
    elif price >= 10 and price < 30:
        return '$$'
    else:
        return '$$$'

def quality(total_bill, tip):
    if tip/total_bill > 0.25:
        return "Generous"
    else:
        return "Other"


# apply custom functions on single column
df = pd.read_csv('auxfiles/tips.csv')

print(df['CC Number'].apply(last_four_digits)) # applies the method to every row in the column
df['yelp'] = df['total_bill'].apply(yelp)
print(df['yelp'])

df['total_bill'].apply(lambda num: num*2) # works with lambdas as well



# apply custom functions on multiple columns
df['Quality'] = df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']), axis=1)
print(df['Quality'])

df['Quality'] = np.vectorize(quality)(df['total_bill'], df['tip']) # decreases computational time by transformal normal functions to numpy-aware functions
print(df)

import timeit
setup = '''
import pandas as pd
import numpy as np
df = pd.read_csv('auxfiles/tips.csv')
def quality(total_bill, tip):
    if tip/total_bill > 0.25:
        return "Generous"
    else:
        return "Other"
'''
stmt_one = '''
df['Quality'] = df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']), axis=1)
'''
stmt_two = '''
df['Quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
'''
print(timeit.timeit(setup=setup, stmt=stmt_one, number=1000))
print(timeit.timeit(setup=setup, stmt=stmt_two, number=1000))



# statistical information and sorting
df = pd.read_csv('auxfiles/tips.csv')
df.describe()
df.describe().transpose()
df.sort_values('tip', ascending=False) # sort, descending order
df.sort_values(['tip', 'size']) # sorts by tip and then size

df['total_bill'].max() # max value
df['total_bill'].idxmax() # index of max value (i.ex. for passing to iloc)

print(df.corr()) # correlation info

df['sex'].value_counts()
print(df['day'].unique()) # name unique values
print(df['day'].nunique()) # count unique values

df['sex'].replace('Female', 'F')
df['sex'].replace(['Female', 'Male'], ['F', 'M'])
mymap = {'Female':'F', 'Male':'M'} # same as above
df['sex'].map(mymap)

simple_df = pd.DataFrame([1,2,2,2],['a','b','c','d'])
simple_df.duplicated() # Series with bool values according to duplicated rows (last two)
simple_df.drop_duplicates()

df['total_bill'].between(10,20,inclusive=True) # Series with bool values according to values within margin

df.nlargest(2, 'tip') # Dataframe with the largest 2 values for 'tip'

df.sample(5) # return dataframe with 5 random rows of the dataframe
df.sample(frac=0.1) # return dataframe with 10% of rows ramndomly of the dataframe