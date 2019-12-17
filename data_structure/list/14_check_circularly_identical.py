"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
 Write a python program to check whether two lists are circularly identical. 
"""
#initializing sample lists on which we haveto check circularity condition
list_one= [10, 10, 0, 0, 10]
list_two = [10, 10, 10, 0, 0]


# function to check circularly identical or not
def check_circularly_identical(list_one,list_two):
    #making a list after doubling the list one
    list_three = list_one*2
    #converting list one into a simple string
    str_list_one =""
    for i in list_one:
        str_list_one=str_list_one+str(i)+" "
    # converting list into a simple string
    str_list_two = ""
    for i in list_two:
        str_list_two=str_list_two+str(i)+" "
    # converting list into a simple string
    str_list_three =""
    for i in list_three:
        str_list_three=str_list_three+str(i)+" "
    #checking if small string is a part of big string
    if str_list_two in str_list_three:
        #printing result
        print("lists are circular")
    else :
        print("lists are not circular")
check_circularly_identical(list_one,list_two)