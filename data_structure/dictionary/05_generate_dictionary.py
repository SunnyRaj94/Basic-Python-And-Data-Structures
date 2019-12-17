"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
"""
#initializing an empty dictionary
my_dictionary = {}
#asking user how many enteries should go in dictionary
entries = int(input("enter number you want to add entries in the dictionary"))

#adding enteries into dictionary
for entry in range(1,entries+1):
    my_dictionary[entry]=entry*entry

#printing the dictionary after adding
print(my_dictionary)