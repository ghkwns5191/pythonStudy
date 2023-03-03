# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 02:33:35 2023

@author: ghkwn
"""





try_input = int(input("내가 생각한 숫자를 맞춰보세요!!"))
answer = 8
                      
if try_input < answer :
    print("입력한 숫자가  너무 작아요")
    
if try_input > answer :
    print("입력한 숫자가 너무 커요")
    
if try_input == answer :
    print("정답입니다!")