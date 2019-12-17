"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python function that takes two lists and returns True if they have at least one common member. 
"""
#initializing a list of strings or words
list_of_words = ['Sunny','Ria','YuvrajSingh', 'BrandonMcculum','Lb','ABD','MSD','Ronaldo']
#initializing 2nd list of words
another_list =['Sunnys','Rias','YuvrajSinghs']
 # method to check if any present
def check_for_presence(list_one,list_two):
    #iterating through 1st list
    for word in list_one:
        #iterating through 2nd list
        for check_for in list_two:
            #checking if word is present
            if word == check_for:
                #returning true if present
                return True
    #returning false if not present
    return False
#method to print output result
def output_result():
    #checking for value if true
    if check_for_presence(list_of_words,another_list)==True:
        print("Word is present in the list")
    else:
        print("word is not present in the list")

#executing script
output_result()
