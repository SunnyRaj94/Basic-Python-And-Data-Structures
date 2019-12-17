"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
"""
#initializing a list of strings or words
list_of_words = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#removing elements from given indexes
list_of_words.pop(0)
list_of_words.pop(3)
list_of_words.pop(3)
#printing the output
print(list_of_words)