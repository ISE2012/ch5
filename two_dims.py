# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:16:12 2020

@author: ucobiz
"""

ex_nums = [[1,2,3,4,5], [6,7,8], [9,0,1,2]]

# 1
for i in ex_nums[0]:
    print(i)

# 2
ex_nums[0][3] = "four"
print(ex_nums)

# 3
ex_nums[2].append(3)
print(ex_nums)

# 4
ex_nums[0].remove(5)
print(ex_nums)
