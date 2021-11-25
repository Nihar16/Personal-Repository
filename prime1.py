# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 12:05:30 2019

@author: Nihar
"""

last=int(input("Enter Range: "))
for x in range(1,last):
    for n in range(2,x):
        if x%n==0:
            print(x," is not Prime as",x,"=",n,"X",x//n)
            break
    else:
        print(x," is Prime")

a=1
b=1
while b < last:
    print(b)
    a,b=b,a+b
   

    