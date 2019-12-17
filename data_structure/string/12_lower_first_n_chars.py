"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to lowercase first n characters in a string
"""
#asking from user to enter a string
my_string = input("enter any string")
#asking from user the limit of first n characters
limit = int(input('Enter the number you want to lowercase till '))
#indexing from 0 to given number
chars_till_limit = my_string[:limit]

#indexing from given number to the end of the string
chars_after_limit = my_string[limit:]

#converting the string to lowercase upto the give number
lower_chars_till_limit=chars_till_limit.lower()

#combing the lists
result_string= lower_chars_till_limit + chars_after_limit

print(result_string)