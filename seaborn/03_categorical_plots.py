# display statistical metrics per category
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dm_office_sales.csv')
sns.countplot() # counts number of rows per category

sns.barplot() # general form of displaying any chosen metric per category