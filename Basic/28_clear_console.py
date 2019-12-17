"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to clear the screen or terminal
"""
#importing inbuilt os module
import os

#sample screen output
a = int(input('Enter a '))
b = int(input('Enter b '))

c = a+b
print(os.name)
print(c)
os.system('clear')
