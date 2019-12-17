"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to remove an item from a tuple
"""
"""
Note: You cannot remove items in a tuple.
Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
"""
#initializing a tuple with different data types
my_tuple =(10,'sunny',22.3,True,1+3j,'h')
#converting tuple to list
my_tuple_list=list(my_tuple)
#removing an element
my_tuple_list.remove(22.3)
#again converting it to tuple
new_tuple = tuple(my_tuple_list)
#printing new tuple
print(new_tuple)