"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python script to sort (ascending and descending) a dictionary by value. 
"""
try:
    #initializing a dictionary
    my_dict={"key1":23,"key2":233,"key3":123,"key4":423,"key5":1}
    #returning a sorted list through sorted function
    sorted_dict=dict(sorted(my_dict.items(),key= lambda key:key[1]))
    #printing the values of sorted dict
    print(sorted_dict)
except Exception:
    print("oops something went wrong")

