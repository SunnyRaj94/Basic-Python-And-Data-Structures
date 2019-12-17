"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to create a symmetric difference.
"""
#creating two sample sets
my_first_set={"apple", "banana", "cherry","potato","xyz"}
my_second_set={"apple","banana"}
#returning symmetric difference of above sets
symmetric_difference_set = my_first_set.symmetric_difference(my_second_set);
#printing the symmetric difference set
print(symmetric_difference_set)