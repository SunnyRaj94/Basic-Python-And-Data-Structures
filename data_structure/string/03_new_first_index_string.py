"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to get a string from a given string where all occurrences 
of its first char have been changed to '$', except the first char itself
"""
#asking from user to enter a string
my_string = input("enter any string")
#initializing new empty string
new_string=my_string[0]
#looping through the indexex
for index in range(1,len(my_string)):
    #checking if it occured again
    if my_string[index] == my_string[0]:
        #changing it to $ sign
        new_string=new_string+'$'
    else:
        new_string=new_string+my_string[index]

#printing the output new string value
print(new_string)