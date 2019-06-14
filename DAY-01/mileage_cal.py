#Gas Mileage Calculator
"""
Created on Mon Jun  3 17:13:29 2019

@author: Himanshu Rathore
"""
# kilometers covered by car
km = float(input("Enter Kilometer>"))
# input of fuel in liters
fuel = float(input("Enter Fuel>"))
# calculating average
average = km/fuel
print("Mileage = ",round(average,2))