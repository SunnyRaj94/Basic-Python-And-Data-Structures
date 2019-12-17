"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to get system command output. 
"""
#importing subprocess inbuilt module
import subprocess
# storing output into variable
returned_text = subprocess.check_output("date")
print("printing command output")
# printing the returned value
print(returned_text.decode("utf-8"))