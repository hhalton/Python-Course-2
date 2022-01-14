# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 16:17:51 2022

by Hazel

Sorting a list
"""
def sort_a_list(a_list):
    b = sorted(a_list, reverse=True)
    print(b)
    
sort_a_list(['b', 'a', 'c'])

def sort_by_mark(my_class):
    a = sorted(my_class, reverse=True)
    print(a)
    
sort_by_mark([(85, 'Susan Maddox'), (6, 'Joshua Tran'), (37, 'Jeanette Wafer')])

def sort_by_name(my_class):
    c = sorted(my_class, key=lambda x: x[1])
    print(c)
    
sort_by_name([(85, 'Susan Maddox'), (6, 'Joshua Tran'), (37, 'Jeanette Wafer')])