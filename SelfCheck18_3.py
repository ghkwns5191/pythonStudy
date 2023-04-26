# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 00:13:15 2023

@author: ghkwn
"""

answer = "apple"
max_tries = 21
tries = 0
guess = input("단어를 맞춰보세요 (총 기회는 " + str(max_tries) +" 번 입니다.) : ")

while guess != answer:
    tries += 1
    if tries > max_tries:
        print("기회를 모두 사용하셨습니다.")
        break
    guess = input("틀렸습니다. 다시 한 번 시도해보세요! (남은 기회는 총 " + str(max_tries - tries) + " 회 입니다.)")

if tries <= max_tries and answer == guess:
    print("정답입니다.")
