# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:05:54 2019

@author: Himanshu Rathore
"""

number_list = input("Enter a space separated list of numbers: ").split()

def Add():
    sum = 0
    for number in number_list:
        sum += int(number)
    return sum

def Multiply():
    product = 0
    for number in number_list:
        product *= int(number)
    return product

sorted_list = sorted(number_list)

def Sorting():
    return sorted_list

def Smallest():
    
    return sorted_list[0]

def Largest():
    return sorted_list[-1]

def Remove_Duplicate():
    list_without_duplicates = list()
    for number in number_list:
        if number not in list_without_duplicates:
            list_without_duplicates.append(number)
    return list_without_duplicates

def Print(list_to_print):
    print("Sum =",Add())
    print("Multiply =",Multiply())
    print("Largest =",Largest())
    print("Smallest =",Smallest())
    print("Sorted =",Sorting())
    print("Without Duplicates =",Remove_Duplicate())    

Print(number_list)