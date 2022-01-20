# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 09:27:00 2022

By Hazel

Exception Handling
"""
import sys
try:
    print(sys.argv[1])
except:
    print("Not enough parameters")