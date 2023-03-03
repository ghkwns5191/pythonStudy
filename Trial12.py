# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 01:47:37 2023

@author: ghkwn
"""

print("Welcome to Mashup Game!")
name1 = input("Enter one full name(FIRST LAST) : ")
name2 = input("Enter another full name(FIRST LAST) : ")

i1 = name1.find(" ")
first1 = name1[0:i1]
last1 = name1[i1 + 1:len(name1) + 1]

i2 = name2.find(" ")
first2 = name2[0:i2]
last2 = name2[i2 + 1:len(name2) + 1]

len_first1 = len(first1)
len_last1 = len(last1)
len_first2 = len(first2)
len_last2 = len(last2)

index_first1 = int(len_first1 / 2)
index_last1 = int(len_last1 / 2)
index_first2 = int(len_first2 / 2)
index_last2 = int(len_last2 / 2)

left_first1 = first1[0:index_first1]
right_first1 = first1[index_first1:len_first1 + 1]
left_last1 = last1[0:index_last1]
right_last1 = last1[index_last1:len_last1 + 1]
left_first2 = first2[0:index_first2]
right_first2 = first2[index_first2:len_first2 + 1]
left_last2 = last2[0:index_last2]
right_last2 = last2[index_last2:len_last2 + 1]


new_name1 = left_first1.capitalize() + right_first2.lower() + " " + left_last1.capitalize() + right_last2.lower()
new_name2 = left_first2.capitalize() + right_first1.lower() + " " + left_last2.capitalize() + right_last1.lower()

print(new_name1)
print(new_name2)