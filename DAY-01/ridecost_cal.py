# Ride Cost Calculator
"""
Created on Mon Jun  3 17:13:29 2019

@author: Himanshu Rathore
"""
# Travelled km in Ride
distance = float(input("Enter distance travelled in Ride>"))
# Calculation of consumed fuel in Ride
consumed_fuel = distance / 18
#Calculation of Ride's Cost
ride_cost = consumed_fuel * 80
print("Ride Cost in INR = ",round(ride_cost,2))