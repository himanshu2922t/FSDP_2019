# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:49:21 2019

@author: Himanshu Rathore
"""
# split() by default returns a list
input_numbers = input("Enter numbers in comma separated form: ").split(",")
print("List:",input_numbers)

# converting list into tuple
print("Tuple: ",tuple(input_numbers))