"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python script to concatenate following dictionaries to create a new one.
"""
#sample dictionaries given in problem
sample_dictionary1={1:10,2:20}
sample_dictionary2={3:30,4:40}
sample_dictionary3={5:50,6:60}

#inserting elements of 2nd dictionary into first
sample_dictionary1.update(sample_dictionary2)
#updating again dictionary 1st
sample_dictionary1.update(sample_dictionary3)
#making a copy of it
concatenated_dictionary = sample_dictionary1.copy()
#printing the concatenated dictionary
print(concatenated_dictionary)