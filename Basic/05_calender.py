"""
Created on 10/12/2019
@author: Sunny Raj
"""
"""
problem statement :
Write a Python program to print the calendar of a given month and year.
"""
# importing TextCalendar class from calendar module
from calendar import TextCalendar as cal

#asking for month input
month = int(input("ENTER month"))
#asking for year input
year = int(input("Enter year"))
#initiallizing the TextCalender
cals = cal(0)
# calling formatmonth method
str=cals.formatmonth(year,month,6,0)
# printing output result
print(str)
