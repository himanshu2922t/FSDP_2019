# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:06:18 2019

@author: Himanshu Rathore
"""

print("Enter persons' details one by one in space separated form-")

person_list = list()
while(True):
    user_input = input("Enter name, age and score: ")
    
    if not user_input:
        break
    
    name, age, score = user_input.split()
    person_list.append((name, age, score))

person_list.sort()
print("Sorted Data:",person_list)