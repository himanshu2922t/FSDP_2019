# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:17:14 2019

@author: Himanshu Rathore
"""
orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
         [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
         [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

# without using lambda,map,list comprehension
output_list = list()
for order in orders:
    for one_item in order[1:]:
        output_list.append( [ order[0], list(one_item)[1]*list(one_item)[2] ] )
print(output_list)
out_dict = {}
for lst in output_list:
    out_dict[lst[0]] = out_dict.get(lst[0], 0) +  lst[1]