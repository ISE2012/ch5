# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:10:27 2020

@author: ucobiz
"""

scores = []
for i in range(5):
    num = 0

    while num <= 0:
        num = int(input("Enter a positive #: "))
    scores.append(num)

print(scores)
