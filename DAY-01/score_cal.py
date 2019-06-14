# Weighted Score Calculator
"""
Created on Mon Jun  3 17:25:45 2019

@author: Himanshu Rathore
"""
# input of assignment marks
print("Enter Marks for-")
assignment1 = int(input("Assignment No. 1 >"))
assignment2 = int(input("Assignment No. 2 >"))
assignment3 = int(input("Assignment No. 3 >"))
# input of Exam Marks
print("Enter Marks for-")
exam1 = int(input("Exam No. 1 >"))
exam2 = int(input("Exam No. 2 >"))
# calculation of weighted score
score = (assignment1 + assignment2 + assignment3)*0.1 + (exam1 + exam2)*0.35
print("Your Weighted Score = ",round(score))