import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# data from https://github.com/CSSEGISandData/COVID-19
file_confirmed = '/projects/covid19/data/time_series_covid19_confirmed_global.csv'
df_confirmed = pd.read_csv(os.getcwd() + file_confirmed)
df_confirmed = df_confirmed.set_index('Country/Region')
df_confirmed = df_confirmed.drop('Province/State', axis=1)
df_confirmed = df_confirmed.drop('Lat', axis=1)
df_confirmed = df_confirmed.drop('Long', axis=1)
fig = plt.figure(figsize=(50,8), dpi=100)
plt.plot(df_confirmed.loc['Afghanistan'])
plt.plot(df_confirmed.loc['Spain'])
plt.xticks(rotation=90) # todo: specify columns as date data type
plt.show()


file_deaths = '/projects/covid19/data/time_series_covid19_deaths_global.csv'
df_deaths = pd.read_csv(os.getcwd() + file_deaths)


file_recovered = '/projects/covid19/data/time_series_covid19_recovered_global.csv'
df_recovered = pd.read_csv(os.getcwd() + file_recovered)
