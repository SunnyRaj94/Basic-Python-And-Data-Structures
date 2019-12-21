"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to clone or copy a list
"""
#creating a list through user input
integer_list = [int(integer) for integer in input("enter integers").split(',')]
#making a copy if interger list
copy_of_integer_list=[]
for value in integer_list:
    copy_of_integer_list.append(value)
#printing it to the consoles
print(copy_of_integer_list)