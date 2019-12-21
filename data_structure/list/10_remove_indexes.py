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
new_list_of_words =[]
for index in range(len(list_of_words)):
    if index==0 or index==4 or index==5:
        pass
    else:
        new_list_of_words.append(list_of_words[index])
#printing the output
print(new_list_of_words)