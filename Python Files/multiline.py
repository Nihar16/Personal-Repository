f=open("multiline.txt", "w+")   #"r+"
print("Enter text on multiple lines. End with # : ")
s=""
while s!="#":
    f.write(s+"\n")
    s=input()

print("The entered text is :")
f.seek(0,0) #seek(offset,fromwhere)
f.read(1)
print(f.readline())
print(f.readlines())
f.seek(0,0)
print(f.read().splitlines())
f.close()
