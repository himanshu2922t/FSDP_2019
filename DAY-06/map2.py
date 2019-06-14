# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:28:52 2019

@author: Himanshu Rathore
"""
names = ['Mary', 'Isla', 'Sam']
print( list( map( lambda name: hash(name), names ) ) )