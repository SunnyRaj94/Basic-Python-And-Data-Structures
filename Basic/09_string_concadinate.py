"""
Created on 11/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to concatenate all elements in a list into a string and return it. 
"""
# creating a list
value_list =[1,2,3,4,5,6,3]

# making an empty string
concat =""

# using for loop to concadinate
for i in value_list:
    concat= concat+str(i)+" "

print(concat)