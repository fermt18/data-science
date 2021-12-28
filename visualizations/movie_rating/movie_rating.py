# Question: is there a conflict of interest for websites both selling movie tickets and displaying movie rates?
# More precisely, is Fandango website artifically rating movies higher in order to get more sales?
# Fandango uses two ratings: STARS (displayed in their website) and RATING (actual true rating displayed in the movie website)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def print_message(message):
    print(message)
    print()

base_path = os.getcwd() + '/visualizations'
fandango = pd.read_csv(base_path + '/movie_rating/data/fandango_scrape.csv')
print_message(fandango.head())
print_message(fandango.describe())
print_message("It is seen that STARS mean tend to be a bit higher than RATING")

print_message("Relationship between ratings and votes")
#sns.scatterplot(data=fandango, y='VOTES', x='RATING')
#plt.show()

print_message("Correlation between columns")
print_message(fandango.corr())
print_message("STARS and RATING are not perfectly correlated")

print_message("Add a new colum to the DF with the Year of the movie")
fandango['YEAR'] = fandango['FILM'].apply(lambda title:title.split('(')[-1].replace(')', '')) # -1 gets last item on the list
print_message(fandango.head())

print_message("How many movies are in the Fandango DF per year?")
print_message(fandango['YEAR'].value_counts())

print_message("What are the 10 movies with the highest number of votes?")
print_message(fandango.nlargest(10, 'VOTES'))

print_message("How many movies have 0 votes?")
no_votes = fandango['VOTES'] == 0
print_message(no_votes.sum())

print_message("Create DF of only reviewe films")
fan_reviewed = fandango[fandango['VOTES'] > 0]
print_message(fan_reviewed.head())

print_message("Diference between STARS and RATING distribution")
#sns.kdeplot(data=fan_reviewed, x='RATING', clip=[0,5], fill=True, label='True Rating')
#sns.kdeplot(data=fan_reviewed, x='STARS', clip=[0,5], fill=True, label='Stars Displayed')
#plt.legend(loc=(1.05, 0.5))
#plt.show()
print_message("There are more RATING scores between 3 and 4 while STARS are mainly found between 4 and 5 where RATING falls sharply")

print_message("Add a column to qunatify the difference between STARS and RATING for each movie")
fan_reviewed['STARS_DIFF'] = (fan_reviewed['STARS'] - fan_reviewed['RATING']).round(2)
print_message(fan_reviewed)

print_message("How many times a certain difference occurs?")
#sns.countplot(data=fan_reviewed, x='STARS_DIFF', palette='magma')
#plt.show()

print_message("There is 1 movie with a whole additional STAR. Which one?")
print_message(fan_reviewed[fan_reviewed['STARS_DIFF'] == 1])


# Comparison of Fandango ratings to other sites
all_sites = pd.read_csv(base_path + '/movie_rating/data/all_sites_scores.csv')
print_message("Explore All sites CSV")
print_message(all_sites.head())

print_message("Rotten Tomatoes: Relationship between  critics and users")
#sns.scatterplot(data=all_sites, x='RottenTomatoes', y='RottenTomatoes_User')
#plt.ylim(0,100)
#plt.show()

print_message("Create a column based on the difference and plot")
all_sites['Rotten_Diff'] = all_sites['RottenTomatoes'] - all_sites['RottenTomatoes_User']
#sns.histplot(data=all_sites, x='Rotten_Diff', kde=True, bins=25)
#plt.show()

print_message("Combine Fandango DF with All Sites DF, and normalize to Fandango STARS and RATINGS 0-5")
df = pd.merge(fandango, all_sites, on='FILM', how='inner')
df['RT_Norm'] = np.round(df['RottenTomatoes']/20, 1) # 0-100
df['RTU_Norm'] = np.round(df['RottenTomatoes_User']/20, 1) # 0-100
df['Meta_Norm'] = np.round(df['Metacritic']/20, 1) # 0-100
df['MetaU_Norm'] = np.round(df['Metacritic_User']/2, 1) # 0-10
df['IMDB_Norm'] = np.round(df['IMDB']/2, 1) # 0-10
print_message(df.head())

print_message("New DF with only the normalized values")
norm_scores = df[['STARS', 'RATING', 'RT_Norm', 'RTU_Norm', 'Meta_Norm', 'MetaU_Norm', 'IMDB_Norm']]
print_message(norm_scores)

print_message("We know that RATING are higher than STARS. But are them also higher than the average?")
print_message("Distribution curves should be evenly distributing along the ratings or normalise around 3 or so")
plt.figure(figsize=(15,6), dpi=200)
sns.kdeplot(data=norm_scores, clip=[0,5], shade=True, palette='Set1')
plt.show()
print_message("Fandango is rating movies much higher, on average")

print_message("Cluster map showing movies by punctuation accross sites")
sns.clustermap(data=norm_scores, cmap='magma', col_cluster=False)
plt.show()
print_message("We can see here also that the worst ratings from other sites get good ratins in Fandango")