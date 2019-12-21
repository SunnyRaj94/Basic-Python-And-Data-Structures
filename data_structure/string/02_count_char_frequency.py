"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to count the number of characters (character frequency) in a string
"""
def my_function():
    # asking from user to enter a string
    my_string = input("enter any string")
    # initializing a dictionary  to store character frequecy
    frequency_dict = {}
    # looping through the index of string
    for characters in my_string:
        # storing it to dictionary
        frequency_dict[characters] = count_char(my_string,characters)

    # printing the dictionary output
    print(frequency_dict)

def count_char(my_string,char):
    count =0
    for val in my_string:
        if val == char:
            count=count +1
    return count

my_function()