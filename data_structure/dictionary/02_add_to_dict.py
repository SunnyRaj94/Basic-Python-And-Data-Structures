"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python script to add a key to a dictionary
"""
#initializing a dictionary
my_dictionary={"key1":"value1","key5":"value5","key4":"value4","key3":"value3","key2":"value2"}
try:
    #asking from user how many values they want to add
    number_of_value=int(input("enter number how many keys you want to add"))
    # looping those number of times
    for number in range(number_of_value):
        #asking for key
        add_key = str(input("enter key name you want to add in dictionary"))
        #asking for value to associate with the key
        add_value = input("enter value you want to associate with that key")
        #adding key:value into the dictionary
        my_dictionary[add_key]=add_value
    #printing the new dict
    print(my_dictionary)
except Exception:
    print("unable to add key/value to the dictionary")