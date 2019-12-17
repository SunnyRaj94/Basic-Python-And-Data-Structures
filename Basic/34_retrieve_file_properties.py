"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to retrieve file properties
"""
#importing os.path and time inbuilt module
import os.path,time
#printing user's environment
path ='/home/admin1/result.txt'
print('File         :', path)
#printing the access time of the file with getatime() method
print('Access time  :', time.ctime(os.path.getatime(path)))
#printing the modification time of the file with getmtime() method
print('Modified time:', time.ctime(os.path.getmtime(path)))
#printing the size of the file
print('Size         :', os.path.getsize(path))