# -*- coding: utf-8 -*-
__author__ = 'Who ?'

import pandas as pd

# Load users info
userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']
users = pd.read_csv('dataSet/users.txt', engine='python',
                    sep='::', header=None, names=userHeader)

# print 10 first users
print('# 10 first users: \n%s' % users[:10])
print('\n==================================================================\n')


# Load ratings
ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('dataSet/ratings.txt', engine='python',
                      sep='::', header=None, names=ratingHeader)

# Example 1: merge tables users + ratings by user_id field
merger_ratings_users = pd.merge(users, ratings)
print('# Merge tables users + ratings by user_id field \n%s' %
      merger_ratings_users[:10])
print('\n==================================================================\n')


# Load movie info
movieHeader = ['movie_id', 'title', 'genders']
movies = pd.read_csv('dataSet/movies.txt', engine='python',
                     sep='::', header=None, names=movieHeader)

# Example 2: merge ratings + users + movies
merge_ratings = pd.merge(pd.merge(users, ratings), movies)
print('# Merge tables ratings + users + movies by user_id and movie_id fields \n%s' %
      merge_ratings[:10])
print('\n==================================================================\n')


# Example 3: Info about specific position (ejem: position 1000)
info1000 = merge_ratings.ix[1000]
print('Info of 1000 position of the table: \n%s' % info1000[:10])
print('\n==================================================================\n')


# Example 4: show specific columns
ratings_info = merge_ratings[['user_id', 'title', 'rating']]
print('Show specific columns: \n%s' % ratings_info[:10])
