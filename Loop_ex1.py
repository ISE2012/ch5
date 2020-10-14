# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 06:37:29 2020

@author: ucobiz
"""

nums  = [98, 75, 89, 100, 45, 82]
total = 0 # we have to initialize total to zero

for n in nums:
    print("Data", n)
    total = total + n   # so that we can use it here
    print("total", total)
    
avg = total / len(nums)
print("Grade average in the class is:", avg)
