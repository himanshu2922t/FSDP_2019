# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:03:44 2019

@author: Himanshu Rathore
"""
string = input("Enter a string: ").lower()

alphabates = 'abcdefghijklmnopqrstuvwxyz'

flag = True
# Checking each alphabate whether it is present in string or not
for char in alphabates:
    #  when any alphabate not present means not pangram hence flag=false and break loop
    if string.find(char) is -1:
        flag = False
        break;        

if flag == True:
    print("PANGRAM")
else:
    print("NOT PANGRAM")
    