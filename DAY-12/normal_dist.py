# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 23:24:43 2019

@author: Himanshu Rathore
"""

# genrating random normally distrubuted data
import numpy as np
incomes = np.random.normal(150, 20, 1000)

# ploting histogram
import matplotlib.pyplot as plt
plt.hist(incomes, 100)
plt.show()

# S.D and variance
print("Standard Deviation is: ", np.std(incomes))
print("Variance is: ", (np.std(incomes))**0.5)