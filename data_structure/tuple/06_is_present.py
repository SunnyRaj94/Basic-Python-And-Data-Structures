"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to check whether an element exists within a tuple.
"""
#initializing a sample tuple to check
numbers_tuple= (1, 2, 3, 4, 4, 5, 29, 56, 3, 5, 2, 86)

#asking from user which element to search
search_element=int(input("enter element you want to search for"))
#checking if element is present in tuple and printing the output
if search_element in numbers_tuple:
    print(search_element,"  is present in tuple")
else :
    print(search_element,"  is not present in tuple")