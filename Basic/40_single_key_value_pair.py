"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to extract single key-value pair of a dictionary in variables
"""
#making a dictionary
d = {1:'Sunny',2:'Shubh',3:'Suresh',4:'Mari',5:'Rajinikant'}
#loop to print the value and key in the dictionary
for k,v in d.items():
    print('Key : {}'.format(k))
    print('Value : {}'.format(v))