"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to remove the first occurrence of a specified element from an array  
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
    #making new array to store array after removal of value
    new_array = array.array('i',[])
    #removing the specified value
    count =0
    for value in elements_array:
        if value==remove_value and count==0:
            count=count+1
            pass
        else:
            new_array.append(value)
    #printing the array after removal
    print("array after removal of element is :",new_array)
except Exception:
    print("oops something went wrong")