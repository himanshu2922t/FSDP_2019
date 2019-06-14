# Replacing of Characters
"""
Created on Mon Jun  3 18:03:48 2019

@author: Himanshu Rathore
"""
# input string
string = input("Enter String>")
# counting total 'R' present in string
total_R = string.count('R')
# Reversing String
rev_str = string [::-1]
# Replacing 'R' in reversed string except Last Occurance
temp_str = rev_str.replace('R','$',total_R-1)
# Reversing temp_str to get required result
string = temp_str [::-1]
print("Replaced String =",string)