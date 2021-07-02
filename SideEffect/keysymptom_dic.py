# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 20:57:58 2021

@author: 
"""


import pandas as pd

df = pd.read_csv('PT_Meds_SE')

#get list of uniques
unique_CID = df['CompoundID'].unique().tolist()
unique_Name = df['Name'].unique().tolist()
unique_ATC = df['ATC'].unique().tolist()
unique_SE = df['Side Effect'].unique().tolist()

#final dictionary
se_names_dic = {}

#set keys and empty lists
for i in unique_SE:
    se_names_dic[i] = []

#populate
for index, row in df.iterrows():
    if(row['Name'] in se_names_dic[row['Side Effect']]):
        continue
    else:
        se_names_dic[row['Side Effect']].append(row['Name'])