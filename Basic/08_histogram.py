"""
Created on 11/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to create a histogram from a given list of integers.
"""
# importing matplot lib to make histograms
import matplotlib.pyplot as plt

# function to take input
def input_val():
    limit = int(input("how many value you want to add"))
    val=[]
    for i in range(0,limit):
        val.append(int(input("enter value")))
    return val

#function to plot the histogram
def plot_histogram():
    val=input_val()
    plt.hist(val,3, facecolor='blue', alpha=0.5)
    plt.show()

plot_histogram()
