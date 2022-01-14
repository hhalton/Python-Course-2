# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 15:09:16 2022

by Hazel
First prime after a number
"""
import math 


def is_prime(n):
    if n==1:
        return False
    if n>1:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i==0:
                return False
        return True
    
Start = 100000000
while is_prime(Start)==False:
    Start = Start+1
print(Start)
    
