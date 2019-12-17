"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python function to find the maximum and minimum numbers from a sequence of numbers
"""
#initializing a list of values
integers= [int(i) for i in input("enter numbers you want to add in list").split()]
#function to find maximum and minimum value in the list
def find_max_and_min():
    max = integers[0]
    min =integers[0]
    for i in integers:
        if i>max:
            max=i
        if i<min:
            min=i
    return max,min

max,min=find_max_and_min()
#printing maximum and minimum values
print("minimum value is : ",min)
print("maximum value is : ",max)
