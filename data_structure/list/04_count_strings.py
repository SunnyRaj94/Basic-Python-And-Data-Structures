"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to count the number of strings where the string length is 2 
or more and the first and last character are same from a given list of strings
"""
# initializing a sample list given in problem
sample_List = ['abc', 'xyz', 'aba', '1221']
# making a function to find expected output
def find_count(sample_list):
    count_string = 0;
    # iterating through elements in string
    for string in sample_List:
        #condition to check
        if len(string) > 2 and string[0] == string[-1]:
            #increasing the count
            count_string = count_string + 1;
    #returning the counted value
    return count_string;
    #printing the output
print("list contains {} numbers of such type of strings".format(find_count(sample_List)))

