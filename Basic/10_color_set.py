"""
Created on 11/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
"""
#creating color sets
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

# finding different elements
diff_set = color_list_1-color_list_2

# printing the output
print(diff_set)
