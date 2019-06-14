# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:08:09 2019

@author: Himanshu Rathore
"""

import re
# input credit cards numbers from user
number_list = list()
while True:
    number = input("Enter your credit card number: ")
    if not number:
        break
    number_list.append(number)

valid_number_list = []
for number in number_list:
    # matching the requirements for float
    valid_num = re.match(r'^[456][0-9]{3}-([0-9]{4}-){2}[0-9]{4}$', number)
    con_num = re.search(r'(\d)\1{3,}',number.replace("-",""))
    if valid_num and not con_num:
        valid_number_list.append("Valid")
    else:
        valid_number_list.append("Invalid")

print(valid_number_list)