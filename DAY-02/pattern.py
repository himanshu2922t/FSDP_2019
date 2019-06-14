# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:02:19 2019

@author: Himanshu Rathore
"""
# input from user 
num = int(input("Enter a number : "))

# printing of first num-1 lines 
for number in range(num):
    print("* " * number)
# printing next num lines
for number in range(num,0,-1):
    print("* " * number)  
    