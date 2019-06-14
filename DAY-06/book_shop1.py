# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:42:19 2019

@author: Himanshu Rathore
"""
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]
  
# without using lambda,map,list comprehension
output_list = []
for item_list in orders:
    if item_list[-1]*item_list[-2] < 100:
        out_tuple = ( item_list[0], round((item_list[-1]*item_list[-2])+10,2) )
    else:
        out_tuple = ( item_list[0], round(item_list[-1]*item_list[-2],2) )
    output_list.append(out_tuple)
print(output_list)

# Using lambda,map,list comprehension
print(list(map(lambda item_list : ( item_list[0], round((item_list[-1]*item_list[-2])+10,2) ) if item_list[-1]*item_list[-2] < 100 else ( item_list[0], round(item_list[-1]*item_list[-2],2) ), orders)))