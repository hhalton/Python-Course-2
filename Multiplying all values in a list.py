# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:48:17 2022

Multiplying all values in a list
"""
def mul(numbers):
    a = len(numbers)
    result = 1
    for i in range(0, a):
        result = result*numbers[i]
    print (result)
        
