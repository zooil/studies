import pandas as pd
import os
encoding = 'latin1'

upath = os.path.expanduser('datasets/movielens/users.dat')
rpath = os.path.expanduser('datasets/movielens/ratings.dat')
mpath = os.path.expanduser('datasets/movielens/movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding)
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding)

print(movies[:5])

data = pd.merge(pd.merge(ratings, users), movies)
print(data.iloc[0])

meam_ratings = mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
print(mean_ratings[:3])

ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10])

active_titles = ratings_by_title.index[ratings_by_title >= 250]
print(active_titles)

mean_ratings = mean_ratings.loc[active_titles]
print(mean_ratings)

top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
print(top_female_ratings[:10])

mean_ratings['diff'] = mean_ratings['M']-mean_ratings['F']

sorted_by_diff = mean_ratings.sort_values(by='diff')
print(sorted_by_diff[:10])

print(sorted_by_diff[::-1][:10])

ratings_std_by_title = data.groupby('title')['rating'].std()
ratings_std_by_title = ratings_std_by_title.loc[active_titles]

print(ratings_std_by_title.sort_values(ascending=False)[:10])
