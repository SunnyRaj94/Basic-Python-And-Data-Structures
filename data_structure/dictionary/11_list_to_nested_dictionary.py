"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to convert a list into a nested dictionary of keys.
"""
#initiallizing sample list
sample_list =[1,2,3,4,5,6,7,8,9,10]
#initializing an empty dictionary
my_dictionary = current = {}
#looping through the list
for value in sample_list:
    #adding key to dict
    current[value] = {}
    #assigning value to thet dict
    current = current[value]
#printing the output dict
print(my_dictionary)