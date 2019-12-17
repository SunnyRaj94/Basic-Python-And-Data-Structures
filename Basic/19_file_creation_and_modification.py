"""
Created on 11/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
 Write a Python program to get file creation and modification date/times.
"""
#importing os and time inbuilt module
import os,time
# getting and printing modified time
print("modified time :", end=" ")
print(time.ctime(os.path.getmtime("05_calender.py"), ))

#getting and printing created time
print("created time :", end=" ")
print(time.ctime(os.path.getctime("05_calender.py"), ))