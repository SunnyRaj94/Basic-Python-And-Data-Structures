"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to print all unique values in a dictionary
"""
#making sample dictionary
sample_data =[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#initializing an empty set for unique values
unique_values = set({})
#looping through sample data
for element in sample_data:
    #iterating through the inside dict
    for value in element.values():
        #adding values to the set
        unique_values.add(value)
#printing the unique values
print(unique_values)
