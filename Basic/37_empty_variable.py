"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to empty a variable without destroying it
"""
#defining variables
n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)

#type() mthod returns the type object
#type()() empty the variable without destroying the variable
n = type(n)()
d = type(d)()
l = type(l)()
t = type(t)()
#displaying values
print(n)
print(d)
print(l)
print(t)