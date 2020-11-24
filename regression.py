# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 23:13:06 2020

@author: Tom
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt

data = pd.read_csv("revs_clean.csv", engine = 'python', na_values = ['..'])
rev = data["Revenue"]
#==============================================================================  
"""Revenue vs. Time"""
time = data["Time convert"]

for i in range(time.size):
    time[i] = (int(time[i][:2]) + int(time[i][3:5])/60)

average = {}
for i, ii in zip(time, rev):
    if i not in average:
        average[i] = [1, ii]
    
    else:
        average[i][0] += 1
        average[i][1] += ii
        
time_u = list(average.keys())
rev_a = []

for i in time_u:
    rev_a.append(average[i][1]/average[i][0])


fig, ax = plt.subplots()
plt.scatter(time_u, rev_a)
plt.plot(time_u, 1079.2305389765409*np.array(time_u) -29036.621431907814 )
plt.xlabel("time")
plt.ylabel("revenue")
ax.set_title("revenue vs. time")
plt.tight_layout()

x = np.array(time_u).reshape(-1, 1)
y = np.array(rev_a).reshape(-1, 1)
    
lm = linear_model.LinearRegression()
model = lm.fit(x, y)

m, b = np.polyfit(time_u, rev_a, 1)
print(lm.score(x,y),"\n")
#==============================================================================    
"""Weekday vs. Time"""
week = data["weekday"]
 
average = {}
for i, ii in zip(week, rev):
    if i not in average:
        average[i] = [1, ii]
    
    else:
        average[i][0] += 1
        average[i][1] += ii
        
week_u = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week_num = [i for i in range(1,8)]
rev_a = []

for i in week_u:
    rev_a.append(average[i][1]/average[i][0])
 
fig2, ax2 = plt.subplots()
plt.xticks(week_num, week_u, rotation=30)
plt.scatter(week_num, rev_a)
plt.plot(week_num, -10489.720482553306*np.array(week_num) + 30818.72336767439 )
#plt.xlabel("weekday")
plt.ylabel("revenue")
ax2.set_title("revenue vs. weekday")
plt.tight_layout() 

x = np.array(week_num).reshape(-1, 1)
y = np.array(rev_a).reshape(-1, 1)

lm = linear_model.LinearRegression()
model = lm.fit(x, y)
m, b = np.polyfit(week_num, rev_a, 1)
print(lm.score(x,y),"\n")
#==============================================================================    
"""Discount Rate vs. Time"""
dis = data["Discount Rate"]
 
average = {}
for i, ii in zip(dis, rev):
    if i not in average:
        average[i] = [1, ii]
    
    else:
        average[i][0] += 1
        average[i][1] += ii
        
dis_u = list(average.keys())
rev_a = []

for i in dis_u:
    rev_a.append(average[i][1]/average[i][0])
 
fig3, ax3 = plt.subplots()
#plt.xticks(week_num, week_u, rotation=30)
plt.scatter(dis_u, rev_a)
plt.plot(dis_u, 234.76817654341093*np.array(dis_u) -23791.829820301227 )
plt.xlabel("discount rate")
plt.ylabel("revenue")
ax3.set_title("revenue vs. discount rate")
plt.tight_layout() 

x = np.array(dis_u).reshape(-1, 1)
y = np.array(rev_a).reshape(-1, 1)

lm = linear_model.LinearRegression()
model = lm.fit(x, y)
m, b = np.polyfit(dis_u, rev_a, 1)
print(lm.score(x,y),"\n")


#==============================================================================
"""Month vs. Time"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

month = data["month"]
average = {}
for i, ii in zip(month, rev):
    if i not in average:
        average[i] = [1, ii]
    
    else:
        average[i][0] += 1
        average[i][1] += ii
        
month_u = list(average.keys())
rev_a = []

for i in months:
    rev_a.append(average[i][1]/average[i][0])
 
fig4, ax4 = plt.subplots()
plt.xticks(list(range(1,13)), months, rotation=90)
plt.scatter(list(range(1,13)), rev_a)
#plt.plot(dis_u, 234.76817654341093*np.array(dis_u) -23791.829820301227 )
#plt.xlabel("discount rate")
plt.ylabel("revenue")
ax4.set_title("revenue vs. month")
plt.tight_layout() 

x = np.array(list(range(1,13))).reshape(-1, 1)
y = np.array(rev_a).reshape(-1, 1)

lm = linear_model.LinearRegression()
model = lm.fit(x, y)
m, b = np.polyfit(list(range(1,13)), rev_a, 1)
print(lm.score(x,y),"\n")

#==============================================================================
"""Unit Price vs. Time"""
up = data["Unit Price"]
average = {}
for i, ii in zip(up, rev):
    if i not in average:
        average[i] = [1, ii]
    
    else:
        average[i][0] += 1
        average[i][1] += ii
        
up_u = list(average.keys())
rev_a = []

for i in up_u:
    rev_a.append(average[i][1]/average[i][0])
 
fig5, ax5 = plt.subplots()
#plt.xticks(list(range(1,13)), months, rotation=90)
plt.scatter(up_u, rev_a)
plt.plot(up_u, 0.3962475765660712*np.array(up_u) -21965.988900497712 )
plt.xlabel("unit price")
plt.ylabel("revenue")
ax5.set_title("revenue vs. unit price")
plt.tight_layout() 

x = np.array(up_u).reshape(-1, 1)
y = np.array(rev_a).reshape(-1, 1)

lm = linear_model.LinearRegression()
model = lm.fit(x, y)
m, b = np.polyfit(up_u, rev_a, 1)
print(lm.score(x,y),"\n")

