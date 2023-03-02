# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:06:03 2023

@author: ghkwn
"""

a = "python 4 ever&EVER 최고!"
print(len(a))

a1 = a.find("E");
print(a1)

a2 = a.find("eve")
print(a2)

a3 = a.rfind("rev")
print(a3)

a4 = a.rfind("VER")
print(a4)

a5 = a.find(" ")
print(a5)

a6 = a.rfind(" ")
print(a6)

a7 = a.find("최")
print(a7)

a8 = a.rfind("고!")
print(a8)

a9 = a.rfind("고최")
print(a9)