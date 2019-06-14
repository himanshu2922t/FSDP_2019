# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:05:28 2019

@author: Himanshu Rathore
"""

def translate(string):
    translated_string = ""
    for char in string:
        if char in ('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'):
            translated_string += char+'o'+char    
        else:
            translated_string += char
    return translated_string
    
input_string = input("Enter a string: ")

print("Translated String:",translate(input_string))