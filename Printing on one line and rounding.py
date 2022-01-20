# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 15:45:27 2022

By Hazel

Printing on one line and rounding
"""

def battery_charge(n):
    rounded_charge = round(n/10)
    print("[", end= "")
    for i in range(0, rounded_charge):
        print("|", end="")
    for j in range(0, 10-rounded_charge):
        print(" ", end="")
    print("]")
    print(n, "%", sep="")
    print()
    
for a in range(0, 101):
    battery_charge(a)
