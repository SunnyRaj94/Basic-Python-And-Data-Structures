"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to create set difference. 
"""
#creating two sample sets
my_first_set={"apple", "banana", "cherry","potato","xyz"}
my_second_set={"apple","banana"}
#returning difference of above sets
difference_set = my_first_set.difference(my_second_set);
#printing the difference set
print(difference_set)