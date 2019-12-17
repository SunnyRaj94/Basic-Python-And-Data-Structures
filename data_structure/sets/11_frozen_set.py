"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to use of frozensets.
"""
#creating sample set
my_set={"apple", "banana", "cherry","potato","xyz"}
#converting it to immutable frozenset
my_frozen_set=frozenset(my_set)
#printing the cleared set
print(my_frozen_set)
# making random sample dictionary
person = {"name": "Sunny", "age": 23, "sex": "male"}
#converting that dictionary into frozen set
person_frozenset = frozenset(person)
#printing frozen set from dictionary it will show only keys
print('The person frozen set is:', person_frozenset)