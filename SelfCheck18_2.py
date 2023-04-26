# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 00:02:48 2023

@author: ghkwn
"""
password = "robot fort flower graph"
space_count = 0
for i in range(len(password)):
    if password[i - 1] == " ":
        space_count += 1

print(space_count)
        