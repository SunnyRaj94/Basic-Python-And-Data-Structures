"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes. 
"""
# importing array module
import array

try:
    #making an array of 5 elements
    arr =array.array('i',[1,2,3,4,5])
    #iterating to get index wise element
    for element in range(len(arr)):
        print(arr[element])
# to catch exception
except Exception:
    print("cant create array")