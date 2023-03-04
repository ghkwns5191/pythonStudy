# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 02:57:48 2023

@author: ghkwn
"""

n = int(input("숫자를 입력하세요"))

for i in range(n,0,-1):
    message = "파이썬 책 " + str(i) + "권이 들어 있는 책장에 파이썬 책이 " + str(i) + "권\n" + "책을 한 권 꺼내 돌려 보고 나니 " + str(i - 1) + "권이 남았네."
    print(str(message))