"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to get the smallest number from a list
"""
#creating a list through user input
integer_list = [int(integer) for integer in input("enter integers").split(',')]

#storing the smallest number in the list into a varible
smallest_value = min(integer_list)

#printing the smallest value
print(smallest_value)