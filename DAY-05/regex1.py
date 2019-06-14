# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:29:33 2019

@author: Himanshu Rathore
"""
import re
# input numbers from user
number_list = list()
while True:
    number = input("Enter a number: ")
    if not number:
        break
    number_list.append(number)

floating_list = []
for number in number_list:
    # matching the requirements for float
    if re.match(r'^[+-]?\d*\.\d+$', number):
        floating_list.append(True)
    else:
        floating_list.append(False)

print(floating_list)