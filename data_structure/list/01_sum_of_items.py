"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to sum all the items in a list.
"""
#creating a list through user input
integer_list = [int(integer) for integer in input("enter integers").split(',')]
#storing the value obtained from sum fumction
sum_of_integers =sum(integer_list)

#printing the sum obtained
print("sum of integers in input list is : ",sum_of_integers)