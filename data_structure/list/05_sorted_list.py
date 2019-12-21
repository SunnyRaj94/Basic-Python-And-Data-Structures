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
sample_List = [(2, 5),(1, 2),(4, 4),(2, 3),(2, 1)]
#returning after sorting the list
for x_index in range(len(sample_List)):
    for y_index in range(len(sample_List)):
        if sample_List[x_index][1]<sample_List[y_index][1]:
            temp = sample_List[x_index]
            sample_List[x_index]=sample_List[y_index]
            sample_List[y_index]=temp
#printing the sorted list
print(sample_List)