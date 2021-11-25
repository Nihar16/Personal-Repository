# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:29:13 2018

@author: Nihar
"""
valid=1
while valid==1:
    print(" ROLL NUMBER DECODER PROGRAM")
    print("=============================")
    roll=input("Enter the Roll No : ")
    if len(roll) != 10:
        valid=0
        print("Invalid Roll No.")
        break
    year='20'+roll[0:2]
    inst=roll[2:3]
    br=roll[3:5]
    div=roll[5:6].upper()
    typ=roll[6:7]

    try:
        runn=int(roll[7:])
    except:
        valid=0
        print("Invalid Roll No.")
        break
    print("Admission Year    :",year)
    if typ=='0':
        print("Admission Type    : FE(UG)")
    elif typ=='1':
        print("Admission Type    : ME(PG)")
    elif typ=='2':
        print("Admission Type    : DSE")
    else:
        valid=0
        print("Invalid Roll No.")
        break

    if inst=='1':
        print("Institute         : VJTI")
    elif inst=='2':
        print("Institute         : WIECT")
    elif inst=='3':
        print("Institute         : TSEC")
    else:
        valid=0
        print("Invalid Roll No.")
        break

    if br=='01':
        print("Branch            : INFT")
    elif br=='02':
        print("Branch            : CMPN")
    elif br=='03':
        print("Branch            : ETRX")
    elif br=='04':
        print("Branch            : EXTC")
    elif br=='05':
        print("Branch            : BIOM")
    else:
        valid=0
        print("Invalid Roll No.")
        break

    print("Division          :", div)
    print("Running No        :",runn)
