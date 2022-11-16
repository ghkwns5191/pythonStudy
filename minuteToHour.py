# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:26:20 2022

@author: ghkwn
"""
import math;

original = 170;
hour = math.floor(original / 60);

minute = original % 60;
print(hour, "시간", minute, "분");