# Finding the sum of n numbers
n=int(input('Enter the number :'))
if (n<=0):
    print("Enter a valid number")
else:
    sum=0
while(n>0):
    sum+=n
    n-=1
print("The sum is : %i" %sum)
