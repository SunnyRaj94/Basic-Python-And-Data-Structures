"""
Created on 10/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
"""
#taking values from input
values=input("input values")
#splitting the values and taking those into list
data = values.split(',')
# making a tuple out of those values
new_data = tuple(data)
print("list data : ", end =" ")
# printing the output
print(data)
print("tuple data : ", end =" ")
# printing the tuple
print(new_data)
