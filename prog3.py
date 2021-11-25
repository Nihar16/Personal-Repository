#Simple program illustrating Input from user

print ("How old are you?")
age = int(input())
print ("How tall are you?")
height = input()
print ("How much do you weigh?")
weight = input()
print ("So, you're %i old, %r tall and %r heavy." % (age, height, weight))
print(age*float(weight))

