# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 23:09:29 2019

@author: Himanshu Rathore
"""
# genrating random incomes
import numpy as np
incomes = np.random.normal(500.0, 100.0, 10000)

# ploting histogram
import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.show()

# mean and median
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))

# adding 100 outliers
for i in range(100):
    incomes = np.append(incomes,5000)
plt.hist(incomes, 50)
plt.show()