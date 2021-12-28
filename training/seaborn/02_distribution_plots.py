import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# rug plot - adds a tick for every value; y axis has no meaning
df = pd.read_csv('auxfiles/dm_office_sales.csv')
plt.figure(figsize=(5,8))
sns.rugplot(x='salary', data=df)
plt.show()

# histogram plot
sns.set(style='darkgrid')
sns.displot(data=df, x='salary', kde=True, rug=True, color='red', edgecolor='blue')
plt.show()

sns.histplot(data=df, x='salary') # the same but more specific
plt.show()

# kde (current density estimation) plot
sns.kdeplot(data=df, x='salary')
plt.show()

np.random.seed(42)
sample_ages = np.random.randint(0,100,200)
sample_ages = pd.DataFrame(sample_ages, columns=['age'])
sns.rugplot(data=sample_ages, x='age')
plt.show()

sns.displot(data=sample_ages, x='age', rug=True, kde=True, bins=30) # kde clipped to values of x
plt.show()

sns.kdeplot(data=sample_ages, x='age', clip=[0,100], bw_adjust=0.01) # bandwith adjust to low values creates skinny gaussian distributions (nore noise); large values tend to show the normalised gaussian distribution
plt.show()
