# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 02:36:46 2023

@author: ghkwn
"""

a = int(input("숫자를 입력하세요"))
message = "안녕"

# for 루프를 이용한 출력
for i in range(a):
    print(message)
    
# for 루프를 이용하지 않고 출력
message_modified = message + "\n"
final_message = message_modified * a
print(final_message[0:len(final_message) - 1])
    
