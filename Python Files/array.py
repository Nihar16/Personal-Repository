from array import *
arr=array('i',[1,34,6,76])
for i in arr:
    print(i)
j="Bottles"
k="Bottle"
for i in range(10,0,-1):
    if (i>=2):
        print(i," Bottles of beer on the wall, ", i," Bottles of beer!!!")
        if(i>2):
            print("Take one down and pass it around and you have ", i-1, "Bottles of beer...")
        else:
            print("Take one down and pass it around and you have ", i-1, "Bottle of beer...")
    else:
        print(i," Bottle of beer on the wall, ", i," Bottle of beer!!!")
        print("Take it down and pass it around and you have no more bottles of beer...")
        
print(" No more Bottles of beer on the wall, No more Bottles of beer!!!")
print("Go to the shop and buy some more, 99 Bottles of beer...")
