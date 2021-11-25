# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 13:01:51 2019

@author: Nihar
"""
good=0
cnt=0
while(not(good)):
    try:
        a=int(input("Enter a No:"))
    except:
        good=0
        print("Expecting an Integer")
    else:
        good=1
    cnt=cnt+1
    if cnt > 5:
        print("Attempts count exceeded...")
        break

