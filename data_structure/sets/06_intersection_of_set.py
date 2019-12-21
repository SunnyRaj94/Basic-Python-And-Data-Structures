"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
 Write a Python program to create an intersection of sets. 
"""
#creating two sample sets
my_first_set={"apple", "banana", "cherry","potato","xyz"}
my_second_set={"apple","banana"}
#returning intersection of above sets
intersection_set = my_second_set & my_first_set

#printing the intersection of sets
print(intersection_set)