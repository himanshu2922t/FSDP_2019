# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:01:52 2019

@author: Himanshu Rathore
"""
# importing calendar class function isleap which check wheather the given year is leap or not
from calendar import isleap
def check_leap(year):
    return isleap(year)     # return (((year%4==0 and year%100!=0) or year%400==0))
# input from user
input_year = int(input("Enter a year : "))
check_leap(input_year)