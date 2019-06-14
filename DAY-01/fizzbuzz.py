# Fizz Buzz
"""
Created on Mon Jun  3 18:54:53 2019

@author: Himanshu Rathore
"""

for counter in range(1,100):
    if(counter%3==0 and counter%5==0):
        print("Fizz Buzz")
    elif(counter%3==0 and counter%5!=0):
        print("Fizz")
    elif(counter%5==0 and counter%3!=0):
        print("Buzz")
    else:
        print(counter)
       