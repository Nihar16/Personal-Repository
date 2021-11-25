def iseven(x):
    return x%2==0
L=[ x**3 for x in range (10)]

print(list(filter(iseven,L)))

def squares(x):
	return x*x
L=[ 1, 2, 3, 4, 5 ]
print ( list ( map ( squares, L ) ) )

L=[ 1, 2, 3, 4, 5 ]
print ( list ( map ( (lambda x : x*x), L ) ) )
Y=[ 6, 7, 8, 9, 10 ]
print ( list ( map ( (lambda x , y : x*y), L, Y ) ) )
