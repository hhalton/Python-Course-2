# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 14:33:22 2022

by Hazel
Print primes between 2 values
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
    
prime_list = []
def primes_in_interval(x, y):
    
    for j in range(x,y):
        if is_prime(j)== True:
            prime_list.append(j)
    return prime_list
 
lst = primes_in_interval(10000,10050)

print(*lst, sep=", ")