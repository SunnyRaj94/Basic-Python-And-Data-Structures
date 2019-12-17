"""
Created on 11/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a python program to access environment variables.  
"""
#importing os inbuilt module
import os

#function to print given enviromnent variable
def func(x):
    print(os.environ[x])

# main runner function to call above function by taking user input
def act():
    variable =input("Enter environment variable")
    func(variable)

act()