"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to remove item(s) from set
"""
#creating a set
my_set=set({"apple", "banana", "cherry","potato","tomato"})

try:
    #asking user which element to remove
    remove_element=input("enter element you want to remove")
    #condition to check if element is present
    if remove_element in my_set:
        # removing element from set
        my_set.remove(remove_element)
        #printing set
        print(my_set)
    else:
        print("element is not present inside the set")
except Exception:
    print("something went wrong")