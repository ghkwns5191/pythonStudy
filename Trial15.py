# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 02:21:57 2023

@author: ghkwn
"""

question1 = input("당신은 배가 고픈가요? (네 / 아니오) : ")
question2 = int(input("초콜릿 바의 가격은 얼마인가요? : "))

if question1 == "네" : 
    if question2 < 1000 : 
        print("초콜릿 바를 전부 구입합니다.")
        
    if question2 >= 1000 and question2 <=5000 :
        print("초콜릿 바를 10개 구입합니다.")
    
    if question2 > 5000 :
        print("초콜릿바를 1개 구입합니다.")
        
print("종료합니다.")
