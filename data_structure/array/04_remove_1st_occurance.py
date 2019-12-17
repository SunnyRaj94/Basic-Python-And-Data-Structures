"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to get the number of occurrences of a specified element in an array.   
"""
# importing array module
import array

try:
    #initializing the array
    elements_array=array.array('i',[])
    #detemining the size of array
    size_of_array=int(input("enter how many values you want to add in array\n"))
    # adding the elements into the array
    for index in range(size_of_array):
        elements_array.append(int(input("enter value")))
    # printing the original array
    print("your entered array is :",elements_array)
    #removing the first occurance value in the array
    remove_value = int(input("enter value you want to remove in this array"))
    #printing the array after removal
    elements_array.remove(remove_value)
    print("array after removal of element is :",elements_array)
except Exception:
    print("oops something went wrong")