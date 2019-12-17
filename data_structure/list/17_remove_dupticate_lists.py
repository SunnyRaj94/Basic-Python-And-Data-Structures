"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
write a Python program to remove duplicates from a list of lists.
"""
#initiallizing a sample list
sample_list =[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
#making a copy of that list
new_unique_list = sample_list.copy()
#checking for duplicacy function
def check_duplicacy(inner_list,given_index):
    #iterating in list using for loop
    for index in range(given_index+1,len(sample_list)):
        #checking if list is duplicated
        if sample_list[index]==inner_list:
            #removing if list is duplicated
            new_unique_list.remove(inner_list)
#driver function to check duplicacy
def obtain_list():
    #loooping through list indexes
    for index in range(len(sample_list)):
        #executing check duplicacy function
        check_duplicacy(sample_list[index],index)

#driving this script
obtain_list()
#printing the result
print(new_unique_list)