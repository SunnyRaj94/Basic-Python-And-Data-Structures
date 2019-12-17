"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to remove a key from a dictionary.
"""
#making sample dictionary
sample_dictionary ={"key1":1,"key2":2,"key3":3,"key4":4,"key5":5,"key6":6,"key7":7}
#removing one key
del sample_dictionary["key7"]
#printing dictionary after removal
print(sample_dictionary)