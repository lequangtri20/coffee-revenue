# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:56:12 2020

@author: Tom
"""

"""
Time convert
weekday 
month 
Empl Name 
Category 
Sub-category 
Glossary 
Product Name 
Unit Price
Quantity
Discount Rate
Payment Methods

"""

import pandas as pd
import math
revenue = pd.read_excel('revenue.xlsx', index_col=None, na_values = ['..'])

#revenue = revenue.sort_values(by = 'Revenue', ascending = True)

time = revenue["Time convert"]
weekday = revenue["weekday"]
empl = revenue["Empl Name"]
cat = revenue["Category"]
sub_cat =  revenue["Sub-category"]
glos = revenue["Glossary"]
prod_name = revenue["Product Name"]
u_price = revenue["Unit Price"]
quan = revenue["Quantity"]
discount = revenue["Discount Rate"]
payment = revenue["Payment Methods"]
month = revenue["month"]

revs = revenue["Revenue"]


time_c =[]
weekday_c = []
empl_c = []
cat_c = []
sub_cat_c = []
glos_c = []
prod_c = []
u_price_c = []
quan_c = []
dis_c  = []
pay_c = []
revs_c = []
month_c = []

for t, w, e, c, s, g, p, u, q, d, p, m, re in zip(time, weekday, empl, cat, sub_cat, glos, prod_name, u_price, quan, discount, payment, month, revs):
    if math.isnan(re):
        continue
    
    time_c.append(t)
    weekday_c.append(w)
    empl_c.append(e)
    cat_c.append(c)
    sub_cat_c.append(s)
    glos_c.append(g)
    prod_c.append(p)
    u_price_c.append(u)
    quan_c.append(q)
    dis_c.append(d)
    pay_c.append(p)
    month_c.append(m)
    revs_c.append(re)
    

    
dic = { "Time convert" :  time_c, "weekday" : weekday_c,"month":month_c ,"Empl Name":empl_c, "Category": cat_c,
     "Sub-category": sub_cat_c, "Glossary" : glos_c, "Product Name":prod_c,"Unit Price": u_price_c,
     "Quantity" : quan_c, "Discount Rate": dis_c, "Payment Methods":pay_c, "Revenue" : revs_c
     }
    
df_c = pd.DataFrame(dic)
df_c.to_csv("revs_clean.csv", index=False)
    
    
    