# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:02:19 2019

@author: Himanshu Rathore
"""

input_list = input("Enter a list of numbers in space separated form:").split()

set_without_duplicates = set(input_list)

list_without_duplicates = list(set_without_duplicates)
print(list_without_duplicates)