# use matplotlibs subplots to create a grid based off a categorical column; similar to hue but in different graphs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('auxfiles/StudentsPerformance.csv')

# only useful if you plan to use the row/col option
sns.catplot(data=df, x='gender', y='math score', kind='box', row='lunch') # using boxplot
plt.show()
sns.catplot(data=df, x='gender', y='math score', kind='box', col='lunch', row='test preparation course')
plt.show()

# pair gridl1 allows to personalise grids
g = sns.PairGrid(df)
g = g.map_upper(sns.scatterplot)
g = g.map_diag(sns.kdeplot)
g = g.map_lower(sns.kdeplot)
g = g.add_legend()
plt.show()