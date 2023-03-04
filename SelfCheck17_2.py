# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 02:48:50 2023

@author: ghkwn
"""

word = input("영단어를 하나 입력하세요")

for v in word:
    if v == "a" or v == "e" or v == "i" or v == "o" or v == "u" :
        print(v, ": vowel")
        
    else :
        print(v, ": ")