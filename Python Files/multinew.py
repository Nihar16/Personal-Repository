import os,sys
while 10:
    nof=input("Enter filename : ")
    if os.path.isfile(nof):
        with open(nof,"r") as f:
            for line in f:
                print(line)
        #sys.exit()
        break
    else:
        print("File Does not exist. Add multiline data. @ termination")
        with open(nof,"w") as w:
            s=""
            while s!="@":
               s=input()
               if s!="@":
                   w.write(s+'\n')
                
