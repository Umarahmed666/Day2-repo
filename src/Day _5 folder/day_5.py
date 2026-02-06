# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 11:41:58 2026

@author: itsom
"""

#functions

def welcome():
    print("welcome to day 5")
    
welcome()    

def good_afternoon():
    print("good afternoon to all")
    
good_afternoon()  

# arguments

def user(name):
    print(name)

user("umar")   

user("amaan")

# 2nd example
#it dont take global variable it takes local variable

x = 10
def show_value():
    x = 5
    print(x)
    
show_value()
print(x)    
    
#using global variabel only

umar = 100
def increase():
    global umar
    umar%=2
    
print(umar)

increase()

#defining functions , using import
#folder, import------ form -------

#importing math

#importing sqrt from math

import math
print(math.sqrt(8))
print(math.remainder(3, 30))

#making it to choose a random name
import random
name = ("talha", "amaan", "sid","akash")
looser =random.choice(name)
print(looser)



#task1
def calc_rectangle(length, width):
    area=length*width
    perimeter = 2*(length+ width)
    return area, perimeter

calc_rectangle(2, 3)

length =int(input("enter length:"))
width = int(input("enter wirdth:"))

area,perimeter = calc_rectangle(length, width)

print("area of rectangle :",area)
print("perimeter of rectangle :",perimeter)


    






















