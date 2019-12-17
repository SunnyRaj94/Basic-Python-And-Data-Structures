"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to create the colon of a tuple.
"""
"""
A copy is sometimes needed so one can change one copy without changing the other.
In Python, there are two ways to create copies :
1.   Deep copy
2.   Shallow copy
In order to make these copy, we use copy module. We use copy module for shallow and deep copy operations
"""
#importing copy module to copy objects
import copy
#initializing a tuple with different data types
my_tuple =(10,'sunny',22.3,[],True,1+3j,'h')

#making a copy object of my tuple
copy_my_tuple = copy.deepcopy(my_tuple)

#appending data inside tuple
copy_my_tuple[3].append("new item")
#printing new copy
print(copy_my_tuple)