"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to get the effective group id, effective user id, 
real group id, a list of supplemental group ids associated with the current process
"""
#importing os inbuilt module
import os
#getegid() method returns the effective group id
print("Effective group id: ",os.getegid())
#geteuid() method returns the effective user id
print("Effective user id: ",os.geteuid())
#getgid() method returns  returns the real group id
print("Real group id: ",os.getgid())
#getgroups() method returns the supplemental group ids
print("List of supplemental group ids: ",os.getgroups())