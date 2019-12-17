"""
Created on 11/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to list all files in a directory in Python. 
"""
#importing os inbuilt module
import os

#making a directory object
file_obj=os.scandir(os.getcwd())

#looping through the object items/ files in directory
for file in file_obj:
    print(file.name)