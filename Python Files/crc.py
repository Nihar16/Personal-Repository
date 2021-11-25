
e = input("\nEnter Key:")
e = [int(i) for i in e]
#---------------sender side-----------------
sdata = input("\nMessage String: ")
d=sdata+("0"*(len(e)-1));c=0

d = [int(i) for i in d]
print("".join([str(i) for i in d]))
for i in range(0,len(sdata)):
  print("-"*len(d))
  print(" "*c+"".join([str(x) for x in d[i:i+len(e)]]))
  if(d[i]>0):
    print(" "*c+"".join([str(i) for i in e]))
    for j in range(0,len(e)):
      d[i+j]^=e[j]
  else:
    print(" "*c+"0"*len(e))
  c+=1
d = "".join([str(i) for i in d])
print("-"*len(d),"\n"," "*(c-1)+d[-(len(e)-1):])

print("\nCRC Code: ",sdata+"".join(d[-(len(e)-1):]))

#---------------receiver side---------------
d = input("\nReceived String: ")

print(d);d = [int(i) for i in d];c=0
for i in range(0,len(d)-len(e)+1):
  print("-"*len(d))
  print(" "*c+"".join([str(x) for x in d[i:i+len(e)]]))
  if(d[i]>0):
    print(" "*c+"".join([str(i) for i in e]))
    for j in range(0,len(e)):
      d[i+j]^=e[j]
  else:
    print(" "*c+"0"*len(e))
  c+=1
d = "".join([str(i) for i in d])
print("-"*len(d),"\n"," "*(c-1)+d[-(len(e)-1):])

if(d[-(len(e)-1):].count("1")>0):
  print("\nCRC Error!")
else:
  print("\nSuccessfull Transmission!")