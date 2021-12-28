# https://seaborn.pydata.org
# https://seaborn.pydata.org/tutorial/color_palettes.html
# statistical plotting library, based on one line code
# built from matplotlib, so plt is still affecting seaborn plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('auxfiles/dm_office_sales.csv')
# relationship between salary and sales?
plt.figure(figsize=(12,4), dpi=200)
sns.scatterplot(
    x='salary', y='sales', data=df, 
    hue='level of education',
    size='salary', # point size according to salary
    palette='Dark2',
    alpha=0.2) # tranparency
plt.savefig('ex5.png')
plt.show()