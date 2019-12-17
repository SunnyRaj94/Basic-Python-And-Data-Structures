"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to remove duplicates from a list
"""
#creating a list through user input
integer_list = [int(integer) for integer in input("enter integers").split(',')]
#converting that list into set to remove duplicates
integer_set = set(integer_list)
#printing the sorted list

print(set(integer_set))