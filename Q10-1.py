# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:12:40 2023

@author: ghkwn
"""

word = "echo"
t = ()
count = 3

t = t + (word,) * 3 + (word[1:4],) * 3 + (word[2:4],) * 3 + (word[3:4],) * 3
print(t)