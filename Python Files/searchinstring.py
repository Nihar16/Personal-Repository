'''s=input("Enter the string : ")
char=input("Enter the character to be found : ")
for i in range(0,len(s)):
    if(s[i]==char):
        print("Found at index position ",i)
        break
    else:
        i=-1
if(i==-1):
    print("The element ",char," is not Found")

a="anuja"
b=ascii(a)
print(type(b))'''



s=input("Enter the string : ")
char=input("Enter the character to be found : ")
for i in s:
    if(char==i):
        print("found")
        break
else:
        i=-1
        print("The element ",char," is not Found")
if(i==-1):
    print("The element ",char," is not Found")
    
