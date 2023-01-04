# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 22:35:01 2023

@author: ghkwn
"""

a = "python 4 ever&EVER. 짱"

# 첫번째 문자만 대문자, 뒤로 소문자
cap = a.capitalize() 
print(cap)

# 소문자를 대문자로, 대문자를 소문자로
swap = a.swapcase()
print(swap)

# 전부 대문자로
upper = a.upper()
print(upper)

#전부 소문자로
lower = a.lower()
print(lower)

