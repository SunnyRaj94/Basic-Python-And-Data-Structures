"""
Created on 12/12/2019
@author: Sunny Raj
"""
"""
Problem Statement:
 Write a Python program to access and print a URL's content to the consol
"""
#importing HTTPConnection
from http.client import HTTPConnection
#creating a connection object
conn = HTTPConnection("www.google.com")
#sending get type of request
conn.request("GET", "/")
#getting response
result = conn.getresponse()
# retrieves the entire contents.
contents = str(result.read())
print(contents)