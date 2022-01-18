# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:05:49 2022

By Hazel

Perfect shuffle
"""

def perfect_shuffle(deck):
    a = len(deck)
    mid = a//2
    first_half = deck[:mid]
    second_half= deck[mid:]
    shuffled = []
    for i in range(0, mid):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])
    print(shuffled)
        
trial = [1, 2, 3, 4, 5, 6]
perfect_shuffle(trial)