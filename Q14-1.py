# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 17:51:46 2023

@author: ghkwn
"""

number1 = int(input("첫 번째 수를 입력하세요 : "))
number2 = int(input("두 번째 수를 입력하세요 : "))

if number1 == number2 :
    print("두 수가 같습니다.")
    
elif number1 > number2 :
    print("두 번째 수가 첫 번째 수보다 작습니다.")
    
elif number2 > number1 :
    print("첫 번째 수가 두 번째 수보다 작습니다.")