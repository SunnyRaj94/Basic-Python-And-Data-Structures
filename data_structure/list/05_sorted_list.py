"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to get a list, sorted in increasing order by the last element in 
each tuple from a given list of non-empty tuples
"""
#making a sample list as given in question
sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#returning sorted list through sorted function
sorted_list = sorted(sample_List,key= lambda x:x[1])
#printing the sorted list
print(sorted_list)