"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged
"""
#asking from user to enter a string
my_string = input("enter any string")
# checks if string length is greater than 3
if len(my_string) >= 3:
    # condition checking if the string ends with 'ing'
    if my_string[-3]=='i' and my_string[-2]=='n' and my_string[-1]=='g':
        my_string = my_string + 'ly'
    else:
        my_string = my_string + 'ing'
else:
    print("please enter a string of minimum length 3")
print(my_string)