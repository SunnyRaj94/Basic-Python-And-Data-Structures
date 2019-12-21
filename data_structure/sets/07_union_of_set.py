"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
 Write a Python program to create an union of sets. 
"""
#creating two sample sets
my_first_set={"apple", "banana", "cherry","potato","xyz"}
my_second_set={"apple","banana"}
#returning union of above sets
union_set = my_first_set | my_second_set

#printing the intersection of sets
print(union_set)