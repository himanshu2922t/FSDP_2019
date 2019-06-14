# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:11:11 2019

@author: Himanshu Rathore
"""

input_list1 = input("Enter a list of numbers in space separated form:").split()
set_of_list1 = set(input_list1)

input_list2 = input("Enter a list of numbers in space separated form:").split()
set_of_list2 = set(input_list2)

intersect_set = set_of_list1.intersection(set_of_list2)
final_list = list(intersect_set)
print(final_list)