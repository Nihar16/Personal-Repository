list=[1,2,3,2,1,4,56,8,7]
newlist=[]
for i in range(0,len(list)):
    if(list[i] in newlist):
        continue
    newlist.append(list[i])
print("old list: \t\t",list)
print("unique elements :",newlist)
