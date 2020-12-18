# allows us to examine data on a per category basis
import numpy as np
import pandas as pd

df = pd.read_csv('auxfiles/mpg.csv')

# evolution of miles per galons (mpg) over years
df['model_year'].value_counts()
df.groupby('model_year') # lazy operation (not done yet)
print(df.groupby('model_year').mean()['mpg']) # model_year becoms the index
print(df.groupby(['model_year', 'cylinders']).mean()) # adding cylinders as subgroup (year -> cylinders)
df.groupby('model_year').describe().transpose()

year_cyl = df.groupby(['model_year', 'cylinders']).mean()
print(year_cyl.index.names) # index names
print(year_cyl.index.levels) # index values
print(year_cyl.loc[[70, 82]]) # sub dataframe with the cylinder data for the year 70 and 82
print(year_cyl.loc[(80,4)]) # series with the data for year 80 and 4 cylinders

print(year_cyl.xs(key=70, level='model_year')) # cross-section that gets a DF with model_year=70; model_year won't appear in the resulting df
print(year_cyl.xs(key=4, level='cylinders')) # cross-section that gets a DF with model_year=70; cylinder won't appear in the resulting df
df[df['cylinders'].isin([6,8])].groupby(['model_year']).mean() # GroupBy multi level not possible - filter first them group
year_cyl.swaplevel() # swaps group and subgroup
year_cyl.sort_index(level='model_year', ascending=False) # sort by index
df.agg(['std', 'mean']) # dataframe with std and mean for each column
df.agg(['std', 'mean'])['mpg'] # series applied to mpg column only
print(df.agg({'mpg':['max', 'mean'], 'weight':['mean', 'std']})) # DF applying aggregation methods to columns