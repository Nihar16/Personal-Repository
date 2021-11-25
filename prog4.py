a=input("First Number  :")
b=input("Second Number :")
c=input("Third Number  :")

if a > b:
	if a > c:
		print("A is Largest")
	elif c > a:
		print("C is Largest")
	else:
		print("Both A and C are Largest")
elif b > a:
	if b > c:
		print("B is Largest")
	elif c > b:
		print("C is Largest")
	else:
		print("Both B and C are Largest")
else:
	if a > c:
		print("Both A and B are Largest")
	elif c > a:
		print("C is Largest")
	else:	
		print("All A, B and C are Same valued")

# people = 30
# cars = 40
# trucks = 15

# if cars > people:
    # print ("We should take the cars.")
    # print("This is it")
# elif cars < people:
    # print ("We should not take the cars.")
    # print("")
# else:
    # print ("We can't decide.")

# if trucks > cars:
    # print ("That's too many trucks.")
# elif trucks < cars:
    # print ("Maybe we could take the trucks.")
# else:
    # print ("We still can't decide.")

# if people > trucks:
    # print ("Alright, let's just take the trucks.")
# else:
    # print ("Fine, let's stay home then.")