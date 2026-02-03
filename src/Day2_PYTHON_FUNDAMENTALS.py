# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 11:39:27 2026

@author: itsom
"""

# task1

name= input("Enter your name:")
age= int(input("Enter your age:"))
age_Final=age+4
print(f"Hey {name}, you will be {age_Final}years old in 2030")


#task 2

amount= float(input("Enter the totala amount:"))
num_of_persons= int(input("Enter the number of persons:"))
amount_to_split=amount/num_of_persons
print(f"Total Bill: {amount}. Each person pays: {amount_to_split}")

#task 3

item_name=("Laptop")
quantity=(2)
price=(499.99)
in_stock=(True)
print(item_name,quantity,price,in_stock)
total_cost=quantity*price
print("total_cost:",total_cost)






