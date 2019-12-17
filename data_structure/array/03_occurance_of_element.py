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
    #initializing element array
    elements_array=array.array('i',[])
    #determining the size of array
    size_of_array=int(input("enter how many values you want to add in array\n"))
    #adding elements into array through user input
    for index in range(size_of_array):
        elements_array.append(int(input("enter value")))
    #counting foa a specific value in the array
    count_value=int(input("enter value you want to count in this array"))
    #printing the counted value
    print("given value is present : ",elements_array.count(count_value)," times in array")

except Exception:
    print("oops something went wrong")