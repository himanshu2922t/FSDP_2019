# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:00:50 2019

@author: Himanshu Rathore
"""
from functools import reduce
reduce( lambda pre_odd,odd : pre_odd*odd, list(filter( lambda number: number%2==1, list(map( int, input("Enter numbers: ").split() )) )) )