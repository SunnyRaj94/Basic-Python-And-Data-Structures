"""
Created on 11/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to check whether a specified value is contained in a group of values. 
"""
#making a list in which we value we have to check
list = [2,3,5,8,9,10,13,45,67,88,98,101,23]
# function to check if value is present in list
def check(true=None):
    val = int(input("Enter number you want to check in list"))
    result = val in list
    if(result==True):
        print("value is present in the list")
    else:
        print("value is not present in the list")

if __name__== '__main__':
    check()
