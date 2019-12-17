"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to count the number occurrence of a specific character in a string
"""
#asking user to take input as main string
main_string =input("enter main string\n")
#asking for input for character you want to count
char = input("enter character you want to count for")
#printing the counted value
print("character is present :",main_string.count(char))