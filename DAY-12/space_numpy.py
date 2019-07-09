# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:15:57 2019

@author: Himanshu Rathore
"""

numbers = list(map(lambda x: int(x) ,input("Enter numbers space separately: ").split()))

import numpy as np
array = (np.array(numbers)).reshape(3,3)