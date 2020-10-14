# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:08:03 2020

@author: ucobiz
"""

num  = 0  # we have to initialize num to zero

while num <= 0:  # so that we can use it here
    num = int(input("Enter a positive number: "))

# the while loop has exited b/c num is positive
print("Thank you.  The number you chose is:", num)

