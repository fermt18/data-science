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

def confirmed_cases_global_by_date(date): #'1/2/21'
    N = len(df_confirmed.columns)
    fig = plt.figure(figsize=(8,10), dpi=150)
    plt.title('Covid-19 Confirmed Cases on: ' + date)
    ax = fig.gca()
    sns.barplot(data=df_confirmed, x=df_confirmed.index, y=date, orient='v')
    plt.xticks(range(N), rotation=90)
    plt.grid()
    ax.margins(x=0)
    ax.set_yscale('log')
    ax.set_xlabel('Countries')
    ax.set_ylabel('Confirmed Cases')
    fig.canvas.draw()
    tl = ax.get_xticklabels()
    maxsize = max([t.get_window_extent().width for t in tl])
    m = 0.1 # inch margin
    s = maxsize/fig.dpi*N+2*m
    margin = m/fig.get_size_inches()[0]
    fig.subplots_adjust(left=margin, right=1.-margin)
    fig.set_size_inches(s, fig.get_size_inches()[0])
    plt.savefig(__file__+".png")
    plt.show()


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

file_deaths = '/projects/covid19/data/time_series_covid19_deaths_global.csv'
df_deaths = pd.read_csv(os.getcwd() + file_deaths)

file_recovered = '/projects/covid19/data/time_series_covid19_recovered_global.csv'
df_recovered = pd.read_csv(os.getcwd() + file_recovered)
