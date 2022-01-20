# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:10:16 2022

By Hazel

Date and Time
"""

import datetime
now = datetime.datetime.now(tz=None)
print("Today is", now.strftime("%Y-%m-%d"), "and it is", 
      now.strftime("%H:%M:%S."))