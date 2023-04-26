# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:51:12 2023

@author: ghkwn
"""

answer = "3"

guess = input("1~14까지의 숫자 중 하나를 맞춰보세요.")
while guess != answer:
    print("틀렸습니다.");
    print(guess);
    guess = input("다시 시도해보세요");
print("맞았습니다.")