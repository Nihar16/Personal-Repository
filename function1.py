# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:58:19 2018

@author: Nihar
"""

#import greeting
import datetime
def greet2(name):
    print("Hello "+ name + ", Good Evening !")
    greet2=len(name)
    return greet2

def greet(name):
    print("Hello "+ name + ", Good Morning !")
    greet=len(name)
    return greet




name1 = input("Enter your Name: ")
hr1 = datetime.datetime.now().hour
if hr1 <= 12:
    x=greet(name1)
else:
    x=greet2(name1)
print(x)
#greet('Radhika')