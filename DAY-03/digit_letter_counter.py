# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:20:48 2019

@author: Himanshu Rathore
"""

input_string = input("Enter a string: ")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

letter_count = 0
digit_count = 0
counter_dict = {}

for char in input_string:
    if char in letters:
        letter_count += 1
        counter_dict[ 'total_letters' ] = letter_count
    elif char in digits:
        digit_count += 1
        counter_dict[ 'total_digits' ] = digit_count

print(counter_dict)