# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 17:54:32 2023

@author: ghkwn
"""

letter = input("영어 문자열을 입력하세요")

if letter.find("a") > 0 or letter.find("e") > 0 or letter.find("i") > 0 or letter.find("o") > 0 or letter.find("u") > 0 :
    print("모든 모음이 들어있습니다.")

if letter[0] == "a" and letter[len(letter) - 1] == "z" :
    print("알파벳 순입니다.")