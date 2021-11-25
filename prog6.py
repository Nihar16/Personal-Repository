i = 0
#Simple while loop
while i<5:
	print('*')
	i+=1

#Loops in lists	
numbers = [] #  This is list
i=0
while i < 6:
    print ("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print ("Numbers now: ", numbers)
    print ("At the bottom i is %d" % i)


print ("The numbers: ")

for num in numbers:
    print (num)
