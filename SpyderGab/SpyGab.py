#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:11:24 2020

@author: Gabriel
"""

import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np


data = pd.read_csv("customers.csv")
print(data.head())
print(data.columns)

    # Takes only staying consumers
loyal_customers = data[data["Churn"] == "No"]
x = loyal_customers['TotalCharges']
y = loyal_customers['tenure']

    #plots
plt.scatter(x.iloc[:500], y.iloc[:500], s=5)
plt.title('Scatter plot')
plt.xlabel('Total Charges')
plt.ylabel('Tenure')
plt.show()