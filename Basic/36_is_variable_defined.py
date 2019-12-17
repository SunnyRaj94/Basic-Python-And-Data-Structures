"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to determine if variable is defined or not
"""
try:
    y  #if y is not defined it returns variable is not defined
    #NameError is a type of error that pops when the variable is not defined
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")