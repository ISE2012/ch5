# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 07:44:37 2020

@author: ucobiz
"""

values = []   # initialize the list to be empty
userVal = 1   # give our loop variable a value

while userVal != 0:
    userVal = int(input("Enter a number, 0 to stop: "))
    if userVal != 0:       # only append if it's valid
        values.append(userVal) # add value to the list

print("Stopped!")
print(values)
