# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 07:18:19 2020

@author: ucobiz
"""

def main():
    print("Welcome to the Grocery Manager v2.0")
    # initialize the value and the size of our list
    grocery_list = [None]*4
    grocerySize = len(grocery_list)
    
    
    for num in range(grocerySize):
        grocery_list[num] = input("Please enter your item:  ")
    
    print(grocery_list)
    
    for item in grocery_list:
        print(item)

main()

