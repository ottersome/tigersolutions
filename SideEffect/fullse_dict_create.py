# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:15:07 2021

@author: 
"""


import pandas as pd

df = pd.read_csv('./SideEffect/common_sideffects')

#get list of uniques
unique_CID = df['CompoundID'].unique().tolist()
unique_Name = df['Name'].unique().tolist()
unique_ATC = df['ATC'].unique().tolist()
unique_SE = df['Side Effect'].unique().tolist()

#final dictionary
name_se_dic = {}

#set keys and empty lists
for i in unique_Name:
    name_se_dic[i] = []

#populate
for index, row in df.iterrows():
    if(row['Side Effect'] in name_se_dic[row['Name']]):
        continue
    else:
        name_se_dic[row['Name']].append(row['Side Effect'])