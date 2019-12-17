"""
Created on 11/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to check whether a file exists
"""
# importing built in module os
import os

# getting / printing current working directory
print(os.getcwd())
#checking if file exists
print(os.path.exists("hello.txt"))