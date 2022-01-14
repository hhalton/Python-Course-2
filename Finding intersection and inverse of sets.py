# -*- coding: utf-8 -*-
"""
# 11/1/22
#By Hazel
# Finding intersection and inverse of sets
"""

def love_meet(bob, alice):
    bob_as_set=set(bob)
    meeting_places=bob_as_set.intersection(alice)
    print(meeting_places)
    return meeting_places


def affair_meet(bob, alice, silvester):
    alice_as_set=set(alice)
    meeting_places2=alice_as_set.intersection(silvester)
    meeting_places2.difference_update(bob)
    print(meeting_places2)
    return meeting_places2

love_meet(['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ'],['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ'])
affair_meet(['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ'],
            ['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ'], 
            ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ'])