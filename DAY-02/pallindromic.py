# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:03:24 2019

@author: Himanshu Rathore
"""
# input from user and storing into a list
my_list = list()
while(True):
    user_input = input()
    if not user_input:
        break
    my_list.append(int(user_input))
    
# for reversing a number in list
def reverse(number):
    str_number = str(number)
    return int(str_number[::-1])

# palindrom check 
def palindrom(tmp_list):
    flag = False
    for number in tmp_list:
        rev_number = reverse(number)
        if rev_number == number:
            flag = True
            break
    if flag == True:
        return True    
    else:
        return False

palindrom(my_list)
    
    
    
 
