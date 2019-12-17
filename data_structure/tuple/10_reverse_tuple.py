"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to reverse a tuple
"""
#initializing a tuple with different data types
my_tuple =(10,'sunny',22.3,True,1+3j,'h')
#converting tuple to list
my_tuple_list=list(my_tuple)
#reversing the list
my_tuple_list.reverse()
#again converting it to tuple
new_tuple = tuple(my_tuple_list)
#printing new tuple
print(new_tuple)