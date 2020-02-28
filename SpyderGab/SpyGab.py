#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:11:24 2020

@author: Gabriel
"""

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


data = pd.read_csv("customers.csv")
print(data.head())
print(data.columns)

    # Takes only staying consumers
loyal_customers = data[data["Churn"] == "No"]
x = loyal_customers['TotalCharges']
y = loyal_customers['tenure']
z = loyal_customers['MonthlyCharges']
Contract = loyal_customers['Contract']



#mtm = 0 #Month to Month Contract
#oney = 0 # One Year Contract
#df.apply(pd.value_counts)twoy = 0 # Two Year Contract

#for i in range(len(x)):
 #   if Contract[i] == 'Month-to-month' : mtm = mtm+1
  #  elif Contract[i] == "One year" : oney = oney+1   
   # elif Contract[i] == "Two year" : twoy = twoy+1
    

        
    
        
    
    

    #plots
#plt.scatter(x.iloc[:500], y.iloc[:500], s=5)
#plt.title('Scatter plot')
#plt.xlabel('Tenure')
#plt.ylabel('Total Charges')
    
x = x[0:200] #check des 500 premières values car l'algo prend du temps
y = y[0:200]
z = z[0:200]

#plt.plot((x),(y)) #Plus les clients sont là longtemps, plus le total charge est haut (logique)
#plt.show()
#plt.plot(x,z)
#plt.show()

