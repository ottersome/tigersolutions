# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:52:44 2021

@author: sergi
"""

import pandas as pd

coms = pd.read_csv('./SideEffect/common_sideffects')
# coms = pd.read_csv('common_sideffects')

#get list of uniques
unique_CID = coms['CompoundID'].unique().tolist()
unique_Name = coms['Name'].unique().tolist()
unique_ATC = coms['ATC'].unique().tolist()

#final dictionary
names_se_dict = {}

#set keys and empty lists
for i in unique_Name:
    names_se_dict[i] = []

#populate
for index, row in coms.iterrows():
    names_se_dict[row['Name']].append(row['Side Effect'])