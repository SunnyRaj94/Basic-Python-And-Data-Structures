"""
Created on 11/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python 21_sort_files_by_date.py. 
"""
#importing time and date module ans os module
import os

# making an object of that file dictionary
obj=os.scandir(os.getcwd())
#making a sorted list based on their creation time
list_obj=sorted(obj, key=lambda i:os.path.getctime(i))
#using for loop to print
for i in list_obj:
    print(i.name)

