# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 22:32:44 2021

@author: Leonard
"""

import numpy as np
import matplotlib.pyplot as plt

import csv

import pandas as pd

df = pd.read_csv('./Kaggle/drugsComTrain_raw.csv')

# #show every meds and symptom
# show_drug_nodupes = df.drop_duplicates('drugName')
# show_symptom_nodupes = df.drop_duplicates('condition')

# #show certain search
# symptom='ADHD'
# x=df[df['condition']=='ADHD'].reset_index()
# y=df[df['drugName'] == 'Guanfacine'].reset_index()
# z = y[y['condition']=='ADHD'].reset_index()

# #listing from higher rating
# review_high_rating = z.sort_values(by=['rating'], ascending=False).review.head()
# show_rating = z.sort_values(by=['rating'], ascending=False).rating.head()
# show_date = z.sort_values(by=['rating'], ascending=False).date.head()

# result = pd.concat([show_date,review_high_rating,show_rating],axis=1)
