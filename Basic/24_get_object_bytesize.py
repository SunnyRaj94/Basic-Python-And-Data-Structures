"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
 Write a Python program to get the size of an object in bytes. 
"""
#importing os module and sys module
import os,sys
#creating an object of current directory
obj=os.scandir(os.getcwd())
#getting the size of object in bytes
print(sys.getsizeof(obj))