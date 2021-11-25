with open("multiline.txt","r") as f:
    print("the no of characters are : ",len(f.read()))
    f.seek(0,0)
    print("the no of lines are : ",len(f.readlines()))
    f.seek(0,0)
    print("the no of words are : ",len(f.read().split(" ")))
    f.seek(0,0)
    print(f.read())
