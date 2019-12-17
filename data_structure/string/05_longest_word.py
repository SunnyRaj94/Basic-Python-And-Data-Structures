"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python function that takes a list of words and returns the length of the longest one
"""
#asking from user to enter a string
my_string = input("enter any string")
#making a list by splitting it through spaces
my_string_list = my_string.split()

#printing word of maximum length
print(max(my_string_list))