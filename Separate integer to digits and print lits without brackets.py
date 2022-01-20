# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 20:56:54 2022

By Hazel

Finding numbers that divide by 7 and sum of digits by 3
"""
final_list=[]
for i in range(0, 1000):
    if i % 7==0:
        num = i
        x = [int(a) for a in str(num)]
        if sum(x) % 3 == 0:
            final_list.append(i)
print(*final_list, sep='\n')


