# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 10:52:04 2019

@author: Nihar
"""

marks=int(input("Enter Marks: "))
if marks >=70:
    print("Congrats!Distinction for you")
elif 70 > marks >= 60:
    print("Well done! First Class !!")
elif 60 > marks >= 40:
    print("You got Second Class")
else:
    print("Sorry! You failed!")
