# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 10:55:13 2026

@author: itsom
"""

#dictionary

student_details = {"name":"Umar", "clsss":5}
print(student_details)
#access value using key
print(student_details["name"])
stu
#updaate and add new key values

#use get()
student_details.get("name")
student_details.get("location",'kalburgi')

#safely iterate using items()
for key,value in student_details.items():
    print(key,value)
    
#avoid key error


#set
values = {1,2,3,3,3,4,5,}
print(values)

a = {1,2,3,4,5,6}
b = {2,4,7,8,9,10}
2 in b
len(a)

print( a|b )
print(a & b)
print(a-b)
print(a^b )



#task 1

contacts = {"umar": 7829114780, "Talha":8873849189, "Afnan":7835264860}
print(contacts)
contacts["maaz"] = 8936218490
contacts["umar"] = 3674123456
print(contacts)
contacts.get("umar",3674123456 )
contacts.get("sohail")
print("contact not found")

for contact,number in contacts.items():
    print(contact,number)
    
    
    
    #task 2

raw_logs =  ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
print(raw_logs)
unique_users=set(raw_logs)
print(unique_users)
print("ID05" in unique_users)
print(len(raw_logs))
print(len(unique_users))
print("3 dublicates was removed")

#task 3

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print("shared interst are",friend_a & friend_b)
print("All hobbies are",friend_a | friend_b)




























