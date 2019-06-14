# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:12:20 2019

@author: Himanshu Rathore
"""
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
print( list( map( lambda name: random.choice(code_names), names ) ) )