def facto(a):
    fact=1
    while(a>0):
        fact*=a
        a-=1
    return fact

b=int(input("enter the number"))
print(f.facto(b))
