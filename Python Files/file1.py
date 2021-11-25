"""f=open("file1.txt", "w")
s=input("Enter text : ")
f.write(s)
f.close()

f=open("file1.txt", "r")
print("The contents of the file are : \n"+f.read())
f.close()
"""


f=open("file1.txt", "a")
s=input("Enter text for appending: ")
f.write("this is text that we entered as text\n")
f.write(s)
f.close()

f=open("file1.txt", "r")
print("The contents of the file are : \n"+f.read(5))
print("Next contents are : "+f.read())
f.close()



