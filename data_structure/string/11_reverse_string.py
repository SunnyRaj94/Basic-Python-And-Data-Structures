"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to reverse a string
"""
#asking from user to enter a string
my_string = input("enter any string")
#initiallizing an empty string
reversed_string = ""
#obtaining reversed string
reversed_string=my_string[-1::-1]
#printing reversed string
print(reversed_string)