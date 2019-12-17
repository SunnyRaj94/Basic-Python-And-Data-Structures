"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to generate all permutations of a list in Python.  
"""
#importing itertools module
import itertools
#initializing a list of strings or words
list_of_words = ['Red', 'Green', 'White']
#taking all permutations of list into a variable
permutation_list=itertools.permutations(list_of_words)
#looping through the permuted list
for permutation in permutation_list:
    #printing each permutation
    print(permutation)
    