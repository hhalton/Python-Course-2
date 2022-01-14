# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 16:44:55 2022

By Hazel

Finding Prime Numbers
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
    
def sum_primes(num):
    Total = 0
    for x in range(2, num):
        if is_prime(x) == True:
            Total= Total + x
    return Total
    
print(sum_primes(12))
