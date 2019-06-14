# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:02:03 2019

@author: Himanshu Rathore
"""
from calendar import isleap
def days_in_month(month,year):
    if(month in ('Jan','Mar','May','Jul','Oct','Dec')):
        return 31
    elif(month in ('Apr','Jun','Aug','Nov')):
        return 30
    else:
        if(isleap(year)):
            return 29
        else:
            return 28

# input from user
month = input("Enter month: ")
year = int(input("Enter year: "))

print(days_in_month(month,year))        