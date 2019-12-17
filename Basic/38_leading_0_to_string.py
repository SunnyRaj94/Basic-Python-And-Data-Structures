"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to add leading zeroes to a string
"""
str_str = 'Welcome'
str_list = str_str.split(' ')
lis = []
num = int(input('Enter the number of zeros you want to add before the string '))
#loop that converts the list of numbers to 0 and stores them in lis variable
for i in range(num):
     lis.append(str(i*0))
#adding the zeros list and string list
add = lis + str_list
words = ' '.join(add)
print(words)