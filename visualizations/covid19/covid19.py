import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

# data from https://github.com/CSSEGISandData/COVID-19
base_path = '/visualizations/covid19/data'
file_confirmed = base_path + '/time_series_covid19_confirmed_global.csv'
df_confirmed = pd.read_csv(os.getcwd() + file_confirmed)
df_confirmed = df_confirmed.set_index('Country/Region')
df_confirmed = df_confirmed.drop('Province/State', axis=1)
df_confirmed = df_confirmed.drop('Lat', axis=1)
df_confirmed = df_confirmed.drop('Long', axis=1)

# Confirmed Cases Evolution
fig = plt.figure(figsize=(25,10), dpi=150)
plt.title('Covid-19 Confirmed Cases')
#countries = df_confirmed.index
countries = ['Spain', 'US', 'Germany', 'India', 'Turkey', 'Brazil']
for country in countries:
    plt.plot(df_confirmed.loc[country], label=country)
plt.plot(df_confirmed.loc[country])
plt.xticks(rotation=90)
ax = fig.gca()
ax.set_xlabel('Dates')
ax.set_ylabel('Confirmed Cases')
ax.legend()
locs, labels = plt.xticks()
for l in labels[::1]:
    l.set_visible(False)
for l in labels[::20]:
    l.set_visible(True)
plt.show()

file_deaths =  base_path + '/time_series_covid19_deaths_global.csv'
df_deaths = pd.read_csv(os.getcwd() + file_deaths)

file_recovered =  base_path + '/time_series_covid19_recovered_global.csv'
df_recovered = pd.read_csv(os.getcwd() + file_recovered)
