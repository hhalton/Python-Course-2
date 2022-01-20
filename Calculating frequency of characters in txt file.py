# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 09:42:31 2022

Find frequency of each letter in txt file
"""
import string
with open("C:/Users/User/Documents/Study/Python Course/Example1.txt", "r") as file1:
    Filecontent = file1.read()
    a = len(Filecontent)
    Count = 0
    for i in range(0, a):
        if Filecontent[i]!= " ":
            Count = Count +1
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    b=len(alphabet_list)
    for j in range(0, b):
        c = Filecontent.count(alphabet_list[j])
        Freq = round(c/Count, 2)
        print(alphabet_list[j], ":", Freq)
