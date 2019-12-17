"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to get numbers divisible by fifteen from a list using an anonymous function
"""
# creating a list of numbers
numbers= [22,4,55,687,998,234,5647,242,21,35,42,120,150,180,210,1500]
#making an anonymous function
result = lambda i:i%15==0
#making list of divisible numbers
div=list(filter(result,numbers))
#printing values
print(div)