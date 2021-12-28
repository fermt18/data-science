# display statistical metrics per category
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# distribution of one category
df = pd.read_csv('auxfiles/dm_office_sales.csv')
sns.countplot(data=df, x='division') # counts number of rows per category, special case for barplot
#  plt.ylim(90,500) # modifies the y axis limits - outcome can be deceiving
plt.show()
print(df['division'].value_counts()) # the same but as table

sns.countplot(data=df, x='level of education', hue='division', palette='Set2')
plt.show()

sns.barplot(data=df, x='level of education', y='salary', estimator=np.mean, ci='sd', hue='division') # generic method, mean salary per ed level, sow std deviation
plt.legend(bbox_to_anchor=(1.05,1))
plt.show()


# distributions accross categories
df = pd.read_csv('auxfiles/StudentsPerformance.csv')
sns.boxplot(data=df, y='math score', x='test preparation course') # distribution of a continuous variable using quartiles (25% data on top, 25% on bottom, 50th percentile as mean (Q2))
plt.show()
sns.boxplot(data=df, y='reading score', x='parental level of education', hue='test preparation course') # prepration course provides better results independently of the parents level of education?
plt.show()

sns.violinplot(data=df, x='reading score', y='parental level of education', hue='test preparation course', split=True, inner='quartile') # probabiliy density accross data using KDE (KDE graph mirrored). Hue splited by the two categories
plt.show()

sns.swarmplot(data=df, x='math score', y='gender', size=2) # shows all data points in a distribution
plt.show()

sns.swarmplot(data=df, x='math score', y='gender', size=2, hue='test preparation course', dodge=True) # hue not really inforative in swarmplot wo dodge
plt.show()

sns.boxenplot(x='math score', y='test preparation course', data=df, hue='gender') # expansion of boxplot using quantiles instead of quartiles
plt.show()
sns.boxplot(x='math score', y='test preparation course', data=df, hue='gender') # quick comparison with boxplot
plt.show()