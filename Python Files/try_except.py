'''while True:
	try:
		x = int(input("Enter a number: "))
		break
	except ValueError:
		print("Not a  valid number. Try again")
'''
def this_fails():
	x = 1/0 
try:
	this_fails()
except ZeroDivisionError as errmsg:
	print('Handling run-time error:', errmsg)

