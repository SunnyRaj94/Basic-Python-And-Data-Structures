"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to multiplies all the items in a list. 
"""
#creating a list through user input
integer_list = [int(integer) for integer in input("enter integers").split(',')]
#making a function to find product of all integers in list
def find_product(integer_list):
    #initializing a product variable
    product=1;
    #looping through list of integers to find product
    for integer in integer_list:
        product = product * integer
    #returning product obtained
    return product

#printing the output obtained
print("product of integers in input list is : ",find_product(integer_list))