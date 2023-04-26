# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 01:36:54 2023

@author: ghkwn
"""

num = 8
guess = int(input("내가 생각한 수를 맞춰보세요 : "))
while guess != num:
    guess = int(input("다시 맞춰보세요 : "))
print("Right!")