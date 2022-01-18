# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 11:51:23 2022

by Hazel

Convert cash amount to coins/notes in different currencies
"""


def how_to_pay(amount, currency):
    Current_total = amount
    Dict={}
    a = len(currency)
    for i in range(a-1, -1, -1):
        if Current_total>= currency[i]:
            b = int(Current_total/currency[i])
            Current_total= Current_total-(b*currency[i])
            Dict[currency[i]]=b
    return Dict
            
euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]

how_to_pay(729, euro)
            
        
        