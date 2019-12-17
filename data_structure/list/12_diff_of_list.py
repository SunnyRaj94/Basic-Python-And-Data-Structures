"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to get the difference between the two lists
"""
#initializing a list of strings or words
list_of_words = ['Sunny','Ria','YuvrajSingh', 'BrandonMcculum','Lb','ABD','MSD','Ronaldo']
#initializing 2nd list of words
another_list =['Sunny','Ria','YuvrajSingh']

#obtaining difference between both lists
difference_list = set(list_of_words)-set(another_list)

#printing the difference list
print(difference_list)