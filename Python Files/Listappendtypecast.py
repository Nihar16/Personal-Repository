from string import *
b=int(input("Enter the size of list : "))
list=[]
r=['0','1','2','3','4','5','6','7','8','9',]
c=1
print("Enter the elements in the list : \n")
for i in range(b):
    a=input()
    if('.' in a):
        t=a.split(".")
        if(len(t)==2):
            for i in t[0]:
                if(i not in r):
                    c=-1
                    break
            for i in t[1]:
                if(i not in r):
                    c=-1
                    break
            if(c != -1):
                list.append(float(a))
            else:
                list.append(a)
        else:
            list.append(a)
    elif(a.isalpha):
        for i in a:
            if(i not in r):
                list.append(a)
                break
        else:
            list.append(int(a))
print(list)
