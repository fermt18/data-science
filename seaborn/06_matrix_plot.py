# visual equivalent of displaying a pivot table
# displays all the data passed in, visualizing all the numeric values in a DataFrame
# all cells should be numbers and same units across the dataframe
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('auxfiles/country_table.csv')
df = df.set_index('Countries')
print(df.head())
# heatmap - visually displays the distribution of cell values with a color mapping
sns.heatmap(df.drop('Life expectancy', axis=1), linewidth=0.5, annot=True, cmap='viridis')
plt.show()

# clustermap - same as heatmap but first conducts hierarchical clustering to reorganize data groups into similar groups
sns.clustermap(df.drop('Life expectancy', axis=1), linewidth=0.5, annot=True, cmap='viridis')
plt.show()