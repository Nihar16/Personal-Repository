sum=0
num=int(input("enter "))
while 1:
    sum+=num
    num-=1
    print(sum)
    if(num==0):
        break
print(sum)
