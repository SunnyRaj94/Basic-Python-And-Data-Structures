"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python function that takes a list of words and returns the length of the longest one
"""
#asking from user to enter a string
my_string = input("enter any string")
#making a list by splitting it through spaces
my_string_list = my_string.split(' ')
longest_word =my_string_list[0]
for index in range(len(my_string_list)):
    if len(longest_word)<len(my_string_list[index]):
        longest_word=my_string_list[index]
#printing word of maximum length
print(longest_word)