# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 07:35:06 2020

@author: ucobiz
"""

date = 0

while date < 1 or date > 31:
    date = int(input("Enter the day: "))

print("Today is Oct", date)