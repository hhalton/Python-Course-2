# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:19:33 2022

By Hazel

Counting occurence of letter in .txt file
"""

with open("C:/Users/User/Documents/Study/Python Course/Example1.txt", "r") as file1:
    Filecontect = file1.read()
    b= Filecontect.count("l")
    print(b)
    