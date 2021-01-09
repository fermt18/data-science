import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

# data from https://github.com/CSSEGISandData/COVID-19
file_confirmed = '/projects/covid19/data/time_series_covid19_confirmed_global.csv'
df_confirmed = pd.read_csv(os.getcwd() + file_confirmed)
df_confirmed = df_confirmed.set_index('Country/Region')
df_confirmed = df_confirmed.drop('Province/State', axis=1)
df_confirmed = df_confirmed.drop('Lat', axis=1)
df_confirmed = df_confirmed.drop('Long', axis=1)
print(df_confirmed.info())
print(df_confirmed.head())

# Confirmed Cases Global by Date
N = len(df_confirmed.columns)
fig = plt.figure(figsize=(8,10)) # blank canvas
ax = fig.gca()
sns.barplot(data=df_confirmed, y=df_confirmed.index, x='1/2/21', orient='h')
plt.yticks(range(N), rotation=0) # add loads of ticks
plt.grid()
ax.margins(y=0)
fig.canvas.draw()
tl = ax.get_yticklabels()
maxsize = max([t.get_window_extent().height for t in tl])
m = 0.2 # inch margin
s = maxsize/fig.dpi*N+2*m
margin = m/fig.get_size_inches()[1]
fig.subplots_adjust(left=margin, right=1.-margin)
fig.set_size_inches(s, fig.get_size_inches()[0])
#plt.savefig(__file__+".png")
plt.show()



file_deaths = '/projects/covid19/data/time_series_covid19_deaths_global.csv'
df_deaths = pd.read_csv(os.getcwd() + file_deaths)

file_recovered = '/projects/covid19/data/time_series_covid19_recovered_global.csv'
df_recovered = pd.read_csv(os.getcwd() + file_recovered)
