# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:04:36 2019

@author: Himanshu Rathore
"""
def bricks_possibility( available_small_bricks, available_big_bricks, row_length):
    required_big_bricks , required_small_bricks = divmod(row_length , 5)

    if required_small_bricks > available_small_bricks or required_big_bricks > available_big_bricks :
        print(False)
    else:
        print(True)
        
user_input = input("Enter small_bricks,big_bricks,row_length: ").split(",")
input_list = [int(number) for number in user_input]

bricks_possibility( input_list[0], input_list[1], input_list[2] )