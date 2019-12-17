"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to find the list of words that are longer than n from a given list of words
"""
#initializing a list of strings or words
list_of_words = ['Sunny','Ria','YuvrajSingh', 'BrandonMcculum','Lb','ABD','MSD','Ronaldo']

#deciding the limit of length input from user
limit_of_length= int(input('Enter your number '))
print("list of words that are longer than ",limit_of_length," words are")
#loop that checks for the length of strings in the list
for i in range(len(list_of_words)):
    #condition to check words length limit
    if len(list_of_words[i]) > limit_of_length:
        #printing those words
        print(list_of_words[i])