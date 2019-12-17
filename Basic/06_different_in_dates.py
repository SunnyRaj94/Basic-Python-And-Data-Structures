"""
Created on 10/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
Write a Python program to calculate number of days between two dates.
"""
# importing date from datetime module
from _datetime import date as dt
#asking from user to enter 1st date
day1 = int(input("Enter 1st date "))

#asking from user to enter 1st month
month1 = int(input("Enter 1st month "))

#asking from user to enter 1st year
year1 = int(input("Enter 1st year"))

#asking from user to enter 2nd date
day2 = int(input("Enter 2nd date "))

#asking from user to enter 2nd month
month2 = int(input("Enter 2nd month "))

#asking from user to enter 2nd year
year2 = int(input("Enter 2nd year"))

#converting input into date object
date1 =dt(year1,month1,day1)
#converting input into date object
date2 =dt(year2,month2,day2)
#getting the difference between date 1 and date2
val =date2-date1
#printing the difference
print(val)
