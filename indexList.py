# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 06:27:37 2020

@author: ucobiz
"""

names = ["Ann", "Bob", "Eve"]
print(names[1], "sends a message to", names[0])
names[0] = "Ann"
print(names[1] + names[1] + names[0] + names[2])
# or     print(names[1]*2 + names[0] + names[2])