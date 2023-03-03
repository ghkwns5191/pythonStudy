# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:37:15 2023

@author: ghkwn
"""

str = "Eat Work Play Sleep repeat"
x1 = str.find("Work")
x2 = str.find(" Sleep")
a = str[x1:x2:1]
b = a.replace("Work", "working")
c = b.replace("Play", "playing")

print(c)