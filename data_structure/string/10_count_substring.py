"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to count occurrences of a substring in a string
"""
#initiallizing a sample string
string = '''
The body was found floating near Hoige Bazar at around 6.30am. The next process will go as per law and 
family members have been informed," Mangaluru police commissioner (city) Sandeep Patil said.
Nethravathi river is located on the outskirts of Mangaluru - 350km from Bengaluru and very close to the Arabian Sea.
'''
#asking the user to enter substring he want to count for
substring = input("enter substring you wnat to count")

#counting and printing the count of substring in sample string
print(string.count(substring))