# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:40:51 2019

@author: Himanshu Rathore
"""

file_name = input("Please enter file name for which you find last line:")

with open(file_name, mode='rt') as file:
    list_of_lines = file.readlines()
    print("Last line:",list_of_lines[-1])