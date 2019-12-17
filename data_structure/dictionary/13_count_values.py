"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to count number of items in a dictionary value that is a list
"""
#making sample dictionary
sample_data =[{"V":"S001","key1":[1,2,2,2]}, {"V": ["S002",6,8]}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#iterating through the list
count_list=0;
for dictionary in sample_data:
    #iterating through each dictionary
    for key,value in dictionary.items():
        if type(dictionary.get(key))==list:
            print(key," have a list in it's value which have  ",len(value)," items")
            count_list=count_list+1;
print("there are :  ",count_list," dictionaries which consists list inside a key")
