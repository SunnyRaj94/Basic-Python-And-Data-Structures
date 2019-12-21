"""
Created on 13/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to reverse the order of the items in the array.
"""
# importing array module
import array

try:
    # making an array of 5 elements
    arr = array.array('i', [1, 2, 3, 4, 5])
    #reversring the array elements
    reverse_array =array.array('i',[])
    #printing reversed array
    for i in range(len(arr) - 1, -1, -1):
        reverse_array.append(arr[i])
    print('Actuacl array : {}'.format(arr))
    print('Reversed array : {}'.format(reverse_array))

except Exception:
    print("oops something went wrong!!!!")