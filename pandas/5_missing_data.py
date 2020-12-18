# real world data will have missing data. We need a strategy for dealing with the gaps (NaN, NaT, ..)
# Keeping the missing data
# PROS
# - Easiest to do
# - does not manipulate or change the true data
# CONS
# - Many methods does not support NaN
# - Often there are reasonable guesses

# Dropping or removing missing data
# PROS
# - Easy to do
# - Can be based on rules
# CONS
# - Potential to lose a lot of data
# - Limits trained models for future data

# Filling the missing data
# PROS
# - Potential to save a lot of data for use in training model
# CONS
# - Hardest to do and somewhat arbitrary
# - Potential to lead to false conclusions
import numpy as np
import pandas as pd

# types for missing data
np.nan
pd.NA 
pd.NaT # not a timestamp

myvar = np.nan
print(myvar == np.nan) # False
print(myvar is np.nan) # True

df = pd.read_csv('auxfiles/movie_scores.csv')
df.notnull() # dataframe with true/false if there is data
print(df.isnull()) # dataframe with true/false if there is no data

df['pre_movie_score'].notnull() # Series of boolean corresponding being notnull = True
print(df[df['pre_movie_score'].notnull()]) # Dataframe applying the previous filter
print(df[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())])

# KEEP DATA
print(df)

# DROP DATA
df.dropna() # drop any row with missing value
df.dropna(thresh=1) # drop any row with all but 1 missing values
df.dropna(axis=1) # drops every column with missing values - every colunm has at least 1 missing value so drops everything
df.dropna(axis=0) # drops every row with missing values
df.dropna(subset=['last_name']) # drop every row with a null value in the last_name column

# FILL DATA
df.fillna('NEW VALUE') # fills any missing value with the value
df['pre_movie_score'].fillna(0) # fills nulls in a given column with the value
df['pre_movie_score'].mean() # average based on existing values
df['pre_movie_score'].fillna(df['pre_movie_score'].mean()) # fill missing values in a column with the mean of the existing values
df.fillna(df.mean()) # applies mean of eaxisting values for each column to missing values when possible (ex. strings are left as NaN)

airline_tix = {'first':100, 'business':np.nan, 'economy-plus':50, 'economy':30}
ser = pd.Series(airline_tix)
print(ser.interpolate()) # fills missing values with the average between two next vlues