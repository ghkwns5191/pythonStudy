# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 01:39:29 2023

@author: ghkwn
"""
import random

intro = input("게임에 참여하시겠습니까? (y or yes / n or no)")
answer = random.randint(0,10)

if intro == 'y' or intro == 'yes':
    print("1부터 10까지의 숫자 중 임의로 한가지 숫자를 생각하고 있습니다.")
    guess = int(input("제가 생각하고 있는 숫자를 맞춰보세요! : "))
    while answer != guess:
        print("틀렸습니다.")
        guess = int(input("다시 한 번 시도해보세요! : "))
    if guess == answer:
        print("축하합니다. 정답입니다!! ")
    