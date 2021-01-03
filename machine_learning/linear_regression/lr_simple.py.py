import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("auxfiles/Advertising.csv")
print(df.info())

df['total_spend'] = df['TV'] + df['radio'] + df['newspaper']
print(df.head())

sns.scatterplot(data=df, x='total_spend', y='sales')
plt.show()
sns.regplot(data=df, x='total_spend', y='sales')
plt.show()

X = df['total_spend']
y = df['sales']

# y = mx+b
# y = B1x + B0
a = np.polyfit(X,y,deg=1) # returns array(B1, B0)

potential_spend = np.linspace(0, 500, 100)
predicted_sales = a[0] * potential_spend + a[1]
plt.plot(potential_spend, predicted_sales)
plt.show()

spend = 200
predicted_sales = a[0] * spend + a[1]
print(predicted_sales)

# y = B3x**3 + B2*x**2 + B1x + B0
aa = np.polyfit(X,y,3)
print(aa) # third polinomial degree. Highest degree polynomials are close to 0 in this case
pot_spend = np.linspace(0, 500, 100)
pred_sales = aa[0] * pot_spend**3 + aa[1] * pot_spend**2 + aa[2] * pot_spend + aa[3]
print(pred_sales)
sns.scatterplot(data=df, x='total_spend', y='sales')
plt.plot(pot_spend, pred_sales, color='red')
plt.show() # now regression is not a straigh line anymore

# which model is best?