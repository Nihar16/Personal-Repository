#-----------------Sender Side-----------------

s = input("\nData: ")

for m in range(0,10):
  if(2**m >= len(s) + m + 1):
    break

code = ["1" for i in range(0,m+len(s))]
for i in range(0,m):
  code[2**i-1] = "0"

k = 0
for i in range(0,len(code)):
  if(code[i] == "1"):
    code[i] = s[k]
    k += 1

pbits = ""
for i in range(0,m):
  p = ""
  for j in range(2**i,len(code)+1,2*2**i):
    p += str(code[j-1 : j+2**i-1])
  code[2**i-1] = str(p.count("1")%2)
  pbits += str(code[2**i-1])
print("\nSent String: ","".join(code))

#-----------------Receiver Side----------------

r = input("\nRecieved String: ")
temp = list(r)

r = list(r)
pbits = ""
for i in range(0,m):
  p = ""
  for j in range(2**i,len(r)+1,2*2**i):
    p += str(r[j-1 : j+2**i-1])
  r[2**i-1] = str(p.count("1")%2)
  pbits += str(r[2**i-1])

if(pbits.count("1")>0):
  pbits = "".join(reversed(pbits))
  pos = int(pbits,2)
  print("\nError At Position",pos)
  if(temp[pos-1]=='0'):
    temp[pos-1]='1'
  else:
    temp[pos-1]='0'
  print("\nCorrected String:","".join(temp))
else:
  print("\nNo Error Found!")