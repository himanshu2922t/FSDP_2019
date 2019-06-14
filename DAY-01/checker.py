# Name Printing Checkerboard pattern
"""
Created on Mon Jun  3 17:38:36 2019

@author: Himanshu Rathore
"""
total_lines = int(input("Enter total no. lines you want in checker >"))
# Take counter for number of lines
counter = 1
while (counter <= total_lines):
    # selects line on even number
    if counter%2==0:
        print(" *" * 8)
    # selects line on odd number
    else:
        print("* " * 8)
    counter+=1