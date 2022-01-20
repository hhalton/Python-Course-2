# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 15:26:50 2022

By Hazel

Getting content of a webpage (scraping)

"""
import requests as req
try:
    webpage = req.get("https://api.github.com/users/python")
    print(webpage.text)
except:
    print("No internet connectivity.")
