"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to print a dictionary in table format
"""
#initializing sample dictionary
sample_dictionary={'Tim':3, 'Kate':2,'sunny':22,'raghav':26,'sana':80,'amitabh':50}
print("name          age")
#looping through the dictionary
for key,value in sample_dictionary.items():
    print(key,"          ",value)