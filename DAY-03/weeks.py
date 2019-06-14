# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:53:41 2019

@author: Himanshu Rathore
"""
# input tuple from user 
existing_days_tuple = tuple(input("Enter existing days in space separated form: ").split())

all_days_in_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

existing_days_list = list(existing_days_tuple)

index = 0
for day in all_days_in_week:
    
    if day not in existing_days_list:
        index = all_days_in_week.index( day )
        existing_days_list.insert( index, day )
        
existing_days_tuple = tuple(existing_days_list)
print(existing_days_tuple)