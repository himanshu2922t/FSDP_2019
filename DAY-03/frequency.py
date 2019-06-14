# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:06:01 2019

@author: Himanshu Rathore
"""

input_string = input("Enter a string: ")

frequency_dict = {}

for char in input_string:
    if char not in frequency_dict:
        frequency_dict[ char ] = 1
    else:
        frequency_dict[ char ] += 1

print(frequency_dict)