"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to iterate over dictionaries using for loops
"""
#making sample dictionary
sample_dictionary ={"key1":1,"key2":2,"key3":3,"key4":4,"key5":5,"key6":6,"key7":7}
#iterarting through the sample dictionary
for key,value in sample_dictionary.items():
    print("for key : ",key,"    ",end="")
    print("value is : ",value)