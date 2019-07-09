# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:23:47 2019

@author: Himanshu Rathore
"""

import numpy as np
array = np.random.randint(5, 15, 40)
# Most frequent value

# using numpy
    # using unique
unique, counts = np.unique(array, return_counts=True)
indeces = np.argmax(counts)
print(unique[indeces])
    # using bincount
np.bincount(array).argmax()

# without using numpy
    # using set (Best in time complexity)
max(map(lambda val: (list(array).count(val), val), set(array)))[1]
    # using Counter
from collections import Counter
Counter(array).most_common()[0][0]
    # using scipy
import scipy.stats
scipy.stats.mode(array)[0][0]