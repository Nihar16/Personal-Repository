name=input("Enter Name :")
ht=""
while ht=="":
    try:
        ht=int(input("Enter Height :"))
    except:
        print("Integer value expected")
wt=""
while wt=="":
    try:
        wt=float(input("Enter Weight :"))
    except:
         print("Numeric value expected")
age=""
while age=="":
        try:
            age=int(input("Enter Age :"))
        except:
            print("Integer value expected")
print (name," is ", age, "years old, weighs",wt,"Kg. and is",ht,"cms. Tall")