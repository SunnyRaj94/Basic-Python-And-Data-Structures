"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to check multiple keys exists in a dictionary.
"""
#initializing a dictionary
my_dictionary={'val_1':8,'val_2':21,'val_3':7,'val_4':20,'val_5':47,'val_6':53,'val_7':29,'val_8':88,'val_9':38}
try:
    #asking user to enter the key name he wants to check for
    check_key=list({'val_1', 'val_2', 'val_3', 'val_4', 'val_5', 'val_6', 'val_7', 'val_8','val'})
    #obtaining result from get method on dictionary
    result =  all(elem in list(my_dictionary.keys()) for elem in check_key)
    #checking if result is none
    if result :
        print("'Given keys are present in the Dictionary'")
    else:
        print("'Given keys are not present in the Dictionary'")
except Exception:
    print("some error occured")