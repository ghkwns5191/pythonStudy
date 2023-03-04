# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 03:15:20 2023

@author: ghkwn
"""

names = input("공백으로 이름을 구분하여 입력하세요 : ")

name = ""
for v in names:
    if v != " " :
        name = name + v
    elif v == " ":
        print("안녕", name)
        name = ""

print("안녕", names[names.rfind(" ") + 1:len(names) + 1])
        

    
    