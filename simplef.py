# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 14:10:27 2019

@author: Nihar
"""

def greet(name):
    print("Hello!", name + " How are you!")


greet("Name")

def ctof(temp1=0):
    ftemp= 9*temp1/5 + 32
    return ftemp
#    print("Farenheit : ", ftemp)
    

print("Temp. in Farenheit is : ",ctof(float(input("Enter Temp. in Celcius: "))))
print(ctof())