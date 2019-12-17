"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to find files and skip directories of a given directory
"""
#importing os module
import os

# This is to get the directory of the folder/file
dir_path = os.getcwd()

for fname in os.listdir(dir_path):
    path = os.path.join(dir_path, fname)
    if os.path.isfile(path):
        print(dir_path + '/' + fname)