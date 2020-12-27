# 2D versions of previous plots
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('auxfiles/StudentsPerformance.csv')

# jointplot - map histograms to each feature of a scatterplot to clarify the distributions within each feature
sns.jointplot(data=df, x='math score', y='reading score')
plt.show()
sns.jointplot(data=df, x='math score', y='reading score', hue='gender')
plt.show()
sns.jointplot(data=df, x='math score', y='reading score', kind='hex') # shows point density by colouring hexagons darker
plt.show()
sns.jointplot(data=df, x='math score', y='reading score', kind='hist')
plt.show()
sns.jointplot(data=df, x='math score', y='reading score', kind='kde', shade=True)
plt.show()


# pairplot - quick way to compare all numerical columns in a DataFrame and check relationships, then dig deeper with jointplot
# creates a historgram for each column and a scatterplot comparison between all possible combinations of columns
# cpu and ram intensive - filter out columns first
sns.pairplot(data=df)
plt.show()
sns.pairplot(data=df, hue='gender', corner=True) # hue here substitutes diagonal histogram by kde for better readiness (force histogram with diag_kind='hist'); corner avoids duplicates on the up on the diagonal
plt.show()
