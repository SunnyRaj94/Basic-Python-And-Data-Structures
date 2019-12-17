"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to find common items from two lists. 
"""
#initializing a list of strings or words
list_of_words = ['Sunny','Ria','YuvrajSingh', 'BrandonMcculum','Lb','ABD','MSD','Ronaldo']
#initializing 2nd list of words
another_list =['Sunny','Ria','YuvrajSingh']

#obtaining common elements in both list
common_elements = list(set(list_of_words).intersection(another_list))

#printing the output
print(common_elements)