"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
 Write a Python program to convert an integer to binary keep leading zeros
"""
# asking for integer input from user
integer = int(input("enter integer value "))
print(format(integer, '08b')) #convering to a 8bit binary format
print(format(integer, '010b'))#converting to a 10bit binary format