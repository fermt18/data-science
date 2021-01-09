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
#fig = plt.figure(figsize=(50,8), dpi=100)
#sns.barplot(data=df_confirmed, y=df_confirmed.index, x='1/2/21', orient='h')
#plt.xticks(rotation=90) # todo: specify columns as date data type
#plt.tick_params(axis='y', which='major', labelsize=7)
#plt.show()

N = 150
data = np.linspace(0, N, N)

plt.plot(data)

plt.xticks(range(N)) # add loads of ticks
plt.grid()

plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2 # inch margin
s = maxsize/plt.gcf().dpi*N+2*m
margin = m/plt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])

plt.savefig(__file__+".png")
plt.show()



file_deaths = '/projects/covid19/data/time_series_covid19_deaths_global.csv'
df_deaths = pd.read_csv(os.getcwd() + file_deaths)

file_recovered = '/projects/covid19/data/time_series_covid19_recovered_global.csv'
df_recovered = pd.read_csv(os.getcwd() + file_recovered)
