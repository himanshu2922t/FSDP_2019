# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:06:43 2019

@author: Himanshu Rathore
"""
number_list =  input("Enter array of numbers space separated: ").split()
# sorting of numbers in another list
sorted_number_list = sorted(number_list)
# removing smallest and largest from sorted list
del sorted_number_list[0]
sorted_number_list.pop()
# average without including smallest and largest
#sum = 0
#for number in sorted_number_list:
#    sum += int(number)
average = sum(sorted_number_list) / len(sorted_number_list)
print("Result:",average)