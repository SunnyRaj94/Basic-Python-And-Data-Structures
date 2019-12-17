"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to get the last part of a string before a specified character
"""
#asking from user to enter a string
my_string = input("enter any string")#sample string input --- https://www.w3resource.com/python-exercises

#splitting the string with the specified delimiter
resulted_string = my_string.split('-')[0]

#printing resulted string
print(resulted_string)