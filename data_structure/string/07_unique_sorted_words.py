"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program that accepts a comma separated sequence of words as input and 
prints the unique words in sorted form (alphanumerically)
"""
#asking from user to enter a string
my_strings = [my_string for my_string in input('Enter comma separated sequence of words ').split(',')]

#sorts the list alphanumerically
my_strings = set(sorted(my_strings))

#printing the output
print(my_strings)