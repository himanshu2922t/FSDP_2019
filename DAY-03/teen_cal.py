# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:13:29 2019

@author: Himanshu Rathore
"""

input_string = input("Enter keys and their values in dictionary format: ")

import ast
teen_dict = ast.literal_eval(input_string)

def fix_teen(value):
    if value in (15,16):
        return value
    else:
        return 0

sum_dict = {'sum':0}
for key , value in teen_dict.items():
    if value in range(13,19):
        teen_dict[ key ] = fix_teen(value) 
    sum_dict[ 'sum' ] += teen_dict[ key ]
        
print(sum_dict)