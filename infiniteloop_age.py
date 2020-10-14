# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 07:38:29 2020

@author: ucobiz
"""

age = 0
while age < 18:   # can’t vote until 18
    age = int(input("What is your age? "))
    print("You can’t vote at age", age)
    # age = age + 1

print("Now you can vote! Yay!")
