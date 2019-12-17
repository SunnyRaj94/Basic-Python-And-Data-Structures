"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to check multiple keys exists in a dictionary.
"""
#initializing a dictionary
my_dictionary={"key1":"value1","key5":"value5","key4":"value4","key3":"value3","key2":"value2"}
try:
    #asking user to enter the key name he wants to check for
    check_key=input("enter the key name you want to search for")
    #obtaining result from get method on dictionary
    result =my_dictionary.get(check_key)
    #checking if result is none
    if result == None:
        print("key is not present in dictionary")
    else:
        print("key is present in the dictionary")
except Exception:
    print("some error occured")