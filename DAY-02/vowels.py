# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:04:10 2019

@author: Himanshu Rathore
"""
# input from user and storing into a list
states = list()
print("Enter States: ")
while(True):
    user_input = input()
    if not user_input:
        break
    states.append(user_input)

index = 0
# selecting each state 
for state in states:
    # converting 
    char_list = list(state)
    for char in char_list:
        if char in ('a','e','i','o','u','A','E','I','O','U'):
            char_list.remove(char)
    states[index] = " ".join(char_list)
    index+=1      

print(states)    