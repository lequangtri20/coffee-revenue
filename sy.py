# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:46:03 2020

@author: Tom
"""

import pandas as pd
data_xls = pd.read_excel('DATA STORE 2.xlsx', index_col=None, na_values = ['..'])


hours = data_xls.iloc[2:,5]
names = data_xls.iloc[2:,11]

current_hour = -1
current_name = ""

employee = {}

for name, convert in zip(names, hours):
    if type(name) == float or type(convert) == float:
        continue
    
    if name != current_name:
        current_hour = -1
    
    
    if name not in employee:
        employee[name] = 1
        current_hour = int(convert[:2])
    
    elif name in employee:
        if int(convert[:2]) != current_hour:
            employee[name] += 1
            current_hour = int(convert[:2])
    
    current_name = name

df = pd.DataFrame({"Employee":employee.keys(), "Total Hours":employee.values()})

df.to_excel("final2.xlsx", index = False)