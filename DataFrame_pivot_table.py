# -*- coding: utf-8 -*-
__author__ = 'Who ?'

import pandas as pd
import numpy as np

# Load Data
userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']
users = pd.read_csv('dataSet/users.txt', engine='python',
                    sep='::', header=None, names=userHeader)

movieHeader = ['movie_id', 'title', 'genders']
movies = pd.read_csv('dataSet/movies.txt', engine='python',
                     sep='::', header=None, names=movieHeader)

ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('dataSet/ratings.txt', engine='python',
                      sep='::', header=None, names=ratingHeader)

# Merge data
mergeRatings = pd.merge(pd.merge(users, ratings), movies)

# Clone DataFrame


def cloneDF(df):
    return pd.DataFrame(df.values.copy(), df.index.copy(), df.columns.copy()).convert_objects(convert_numeric=True)


# Simple pivot (Groupby + avg)
df_1 = cloneDF(mergeRatings)
df_1 = df_1.pivot_table(index=['movie_id', 'title'])
print('Columns(movie_id + title) to Index: \n%s' % df_1[:5])
print('\n==================================================================\n')


# Pivot by specific columns (Groupby + avg by rating and age)
df_2 = cloneDF(mergeRatings)
df_2 = df_2.pivot_table(index=['movie_id', 'title'], values=['rating', 'age'])
print('Columns(movie_id + title) to Index and avg by values \n%s' % df_2[:5])
print('\n==================================================================\n')


# Pivot by specific columns, applying a functions
df_3 = cloneDF(mergeRatings)
df_3 = df_3.pivot_table(index=['movie_id', 'title'], values=[
                        'rating'], aggfunc=[np.sum, np.size, np.mean])
print('Columns(movie_id + title) to Index and specific functions by values \n%s' %
      df_3[:5])
print('\n==================================================================\n')


# Pivot by specific index, specific values and specific columns, applying a functions
df_4 = cloneDF(mergeRatings)
df_4 = df_4.pivot_table(index=['movie_id', 'title'], values=['rating'], columns=['gender'], aggfunc=[np.mean],
                        fill_value=-1, margins=True)
print('Columns(movie_id + title) to Index and avg rating applied by gender \n%s' %
      df_4[:5])
