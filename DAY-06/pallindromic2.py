# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:02:12 2019

@author: Himanshu Rathore
"""
input_numbers = input("Enter numbers: ").split()
print(all( [int(number)>0 for number in input_numbers] ) and 
      any( map( lambda number: True if str(number)[::-1] == str(number) else False, map( int, input_numbers ) ) ) )