"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to count the values associated with key in a dictionary.
"""
#initializing sample dictionary
sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
#initializing a variable to count the success occurence
count_success=0;
#looping through the dictionary
for dictionary in sample_data:
    #printing keys and count of values associated in it
    for key,value in dictionary.items():
        #condition to check if key is success
        if key =='success':
            #condition to check if associated value is true
            if dictionary.get(key)== True:
                count_success=  count_success+1
# printing the count of success those are set as true
print(count_success,"  success values are associated with True value in present list")