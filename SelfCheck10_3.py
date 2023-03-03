# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:00:48 2023

@author: ghkwn
"""

a = ("abc", (1,2,3))[1]
print(a)

a = ("abc", (1,2,"3"))[1][2]
print(a)

a = ("abc", (1,2), "3", 4, ("5", "6"))[1:3]
print(a)

a = 0
t = (True, "True x")
x = t[a]
print(x)

