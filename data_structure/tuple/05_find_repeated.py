"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to find the repeated items of a tuple
"""
#initializing a sample tuple to check
numbers_tuple= (1, 2, 3, 4, 4, 5, 29, 56, 3, 5, 2, 86)
#initializing a new list to store repeated elements
list_of_repeated = []
# loop for checking repeated items in a tuple
for index in range(len(numbers_tuple)):
    #checking repeadency
    if numbers_tuple.count(numbers_tuple[index]) > 1:
        #appending to list
        list_of_repeated.append(numbers_tuple[index])

# prnting after converting it to sets
print(tuple(set(list_of_repeated)))