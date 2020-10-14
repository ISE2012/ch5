# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 06:41:45 2020

@author: ucobiz
"""

str = "jazz"
print("Original word =", str)


# Loops
reversedString = ""
index = len(str) # calculate length of string and save in index
while index > 0: 
    reversedString += str[index - 1] # save the value of str[index-1] in reverseString
    print("temp reverse result:", reversedString) # printing the temporary result of reversing word
    index = index - 1 # decrement index
    print("Index value:", index)
    
print("Reversed with Loops =", reversedString) # reversed string

