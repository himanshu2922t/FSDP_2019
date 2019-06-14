# String Handling
"""
Created on Mon Jun  3 19:06:12 2019

@author: Himanshu Rathore
"""
string = input("Enter Your Name>")
space_index = string.index(" ")
print(string[space_index+1:],string[:-space_index])