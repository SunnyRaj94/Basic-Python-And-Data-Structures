"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to reverse the order of the items in the array.
"""
# importing array module
import array

try:
    # making an array of 5 elements
    arr = array.array('i', [1, 2, 3, 4, 5])
    #reversring the array elements
    arr.reverse()
    #printing reversed array
    for index in range(len(arr)):
        print("element at : ",index," is ",arr[index])

except Exception:
    print("oops something went wrong!!!!")