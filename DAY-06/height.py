# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:30:58 2019

@author: Himanshu Rathore
"""

people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]
height_total = 0
height_count = 0

from functools import reduce
for person in filter( lambda person: 'height' in person , people):
    height_total += person['height']
    height_count += 1
reduce( lambda height_total, height_count: height_total / height_count if height_count>0 else 0, [height_total,height_count] )