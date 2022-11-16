# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:34:10 2022

@author: ghkwn
"""
import math;

original1 = 456;
original2 = 0;
original3 = 9999;

hour1 = math.floor(original1 / 60);
minute1 = original1 % 60;

print(original1, "분은 ", hour1, "시간", minute1, "분 입니다.");

hour2 = math.floor(original2 / 60);
minute2 = original2 % 60;

print(original2, "분은 ", hour2, "시간", minute2, "분 입니다.");

hour3 = math.floor(original3 / 60);
minute3 = original3 % 60;

print(original3, "분은 ", hour3, "시간", minute3, "분 입니다.");
