"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to create a dictionary from a string.Track the count of the letters from the string
"""
#making sample string
sample_string = 'w3resource'
#initializing an empty dictionary
count_dictionary={}
#indexing through the string
for index in range(len(sample_string)):
    #adding element + their count in the dictionary
    count_dictionary[sample_string[index]]=sample_string.count(sample_string[index])

#printing the resulted dictionary
print(count_dictionary)