"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
 Write a Python program to get the name of the host on which the routine is running.
"""
#importing socket module
import socket
#getting the host name
host_name = socket.gethostname()
#printing the host name
print("Host name:", host_name)
print()