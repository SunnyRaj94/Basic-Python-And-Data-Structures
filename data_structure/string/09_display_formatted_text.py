"""
Created on 14/12/2019
@author: Sunny Raj
"""
"""
problem statement:
Write a Python program to display formatted text (width=50) as output
"""
#importing textwrap which helps us in do text formatting work done
import textwrap
#initiallizing a string
string = '''
The body was found floating near Hoige Bazar at around 6.30am. The next process will go as per law and 
family members have been informed," Mangaluru police commissioner (city) Sandeep Patil said.
Nethravathi river is located on the outskirts of Mangaluru - 350km from Bengaluru and very close to the Arabian Sea.
'''
#fill() method takes the given string and prints within the given width
print(textwrap.fill(string, width=50))