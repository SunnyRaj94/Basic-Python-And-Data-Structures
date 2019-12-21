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
smallest_value = integer_list[0]
for value in integer_list:
    if value>smallest_value:
        smallest_value=value


#printing the smallest value
print(smallest_value)