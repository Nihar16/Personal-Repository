#Prime numbers in the range 2 to 10
for n in range(2, 20):
	prime=1
	for x in range(2, n):
		if n % x == 0:
			print('The number',n, 'is Not Prime as it equals', x, '*', n//x)
			prime=0
			break
	if(prime==1):
		print("The number %d is Prime"%n)
		
		