"""
Created on 11/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
 Write a program to get execution time for a Python method. 
"""
#importing time module
import time
#time() method stores the number of seconds passed since epoch
start_time = time.time()
print(start_time)
#Sample program
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

list3 = color_list_2-color_list_1
print(set(list3))

#time difference between before and after executing the rogram
total_time = time.time() - start_time

print("{} seconds".format(total_time))