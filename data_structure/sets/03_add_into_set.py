"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
 Write a Python program to add member(s) in a set.
"""
#creating a set
my_set=set({"apple", "banana", "cherry","potato","tomato"})

#asking from user how many elements you want to add
numbers = int(input("enter how many elemnts you want to add"))

#looping to add members to set
for number in range(numbers):
    add_element =input("enter value you want to add")
    #adding item into set
    my_set.add(add_element)
#printing after adding element
print(my_set)