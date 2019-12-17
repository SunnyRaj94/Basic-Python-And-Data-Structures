"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to unpack a tuple in several variables. 
"""
#initializing a tuple with different data types
my_tuple =(10,'sunny',22.3,True,1+3j,'h')
#unpacking the values of tuple a into different variables
(first_element,sec_element,third_element,fourth_element,fifth_element,sixth_element) = my_tuple

#printing elements one by one
print(first_element)
print(sec_element)
print(third_element)
print(fourth_element)
print(fifth_element)
print(sixth_element)