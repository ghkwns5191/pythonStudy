# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 02:55:24 2023

@author: ghkwn
"""
count = 0
for v in range(2,101,2):
    if v % 6 == 0 :
        count += 1

print(count)