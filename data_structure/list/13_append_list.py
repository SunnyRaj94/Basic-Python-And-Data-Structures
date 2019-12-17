"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to append a list to the second list
"""
#initializing a list of strings or words
list_of_words = ['Sunny','Ria','YuvrajSingh', 'BrandonMcculum','Lb','ABD','MSD','Ronaldo']
#initializing 2nd list of words
another_list =['ramu','shamu','chomu']
#obtaining appended list
list_of_words.extend(another_list)
#printing appended list
print(list_of_words)