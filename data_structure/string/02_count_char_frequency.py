"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to count the number of characters (character frequency) in a 
"""
#asking from user to enter a string
my_string = input("enter any string")
#initializing a dictionary  to store character frequecy
frequency_dict={}
#looping through the index of string
for characters in my_string:
    #storing it to dictionary
    frequency_dict[characters]=my_string.count(characters)

#printing the dictionary output
print(frequency_dict)