# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:58:15 2019

@author: Himanshu Rathore
"""

with open ('absentee.txt', mode='wt') as file:
    input_counter=0
    while(True):
        student_name = input("Enter name: ")
        input_counter +=1
        if not student_name:
            break
        elif input_counter>15:
            print("Maximum input limit = 15")
            break
        else:
            file.write(student_name+'\n')

with open ('absentee.txt', mode='rt') as file:
    print(file.read())