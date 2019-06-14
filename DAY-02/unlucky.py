# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:07:25 2019

@author: Himanshu Rathore
"""

print("Enter number series space saparated: ")
input_numbers = input().split()

sum=0
pre_number_flag = False
for number in input_numbers:
    if int(number)==13:
        pre_number_flag = True
    elif not pre_number_flag:
        sum += int(number)
    else:
        pre_number_flag = False
print("Result:",sum)
    