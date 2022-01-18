# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 14:37:17 2022

By Hazel

Converting Roman Numerals to Arabic numbers
"""

def from_roman_numeral(roman_numeral):
    list1=[]
    list1[:0]=roman_numeral
    a = len(list1)
    for i in range(0, a):
        if list1[i]=='I':
            list1[i]= 1
        elif list1[i]=='V':
            list1[i]= 5
        elif list1[i]=='X':
            list1[i]= 10
        elif list1[i]=='L':
            list1[i]= 50
        elif list1[i]=='C':
            list1[i]= 100
        elif list1[i]=='D':
            list1[i]= 500
        elif list1[i]=='M':
            list1[i]= 1000
    print(list1)
    for j in range(1, a):
        if list1[j-1]<list1[j]:
            list1[j-1]= list1[j-1]*-1
    print(list1)
    print(sum(list1))
    return sum(list1)
     
from_roman_numeral('MCM')