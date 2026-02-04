# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 11:10:06 2026

@author: itsom
"""

 #list,
 
fruits = ["apple"," banana", "grapes"]
print(fruits)
 
fruits.append("chiku")
print(fruits)
 
fruits.pop(0)
print(fruits) 
#sort
fruits.sort()
print(fruits) 

#slice
fruits[0:3]

fruits.index("grapes")
print(fruits)
 
#task1
inventory_containing = ["Apples", "Bananas", "Carrots", "Dates"]
print(inventory_containing)
inventory_containing.append("Eggs")
print(inventory_containing)
inventory_containing.remove("Bananas")
inventory_containing.sort()
print(inventory_containing)


#task 2
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
temperatures[0]
temperatures[-1]

Afternoon_Peak = temperatures[3:6]
print(Afternoon_Peak)
last_3_hours = temperatures[-3:]
print(last_3_hours)

print(temperatures)
print(Afternoon_Peak)
print(last_3_hours)

#task 3
screen_res = (1920, 1080)
print("Current Resolution: 1920x1080")
print(screen_res)
screen_res[0] = 1280
print("Tuples cannot be modified")

















 