"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to get the command-line arguments (name of the script,
the number of arguments, arguments) passed to a script.
"""
# importing sys module
import sys

#printing command line arguments
#sys.argv returns system arguments
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , sys.argv)