import sqlite3
#import pwd

myemp=99999
while myemp != 0:
	myemp = int(input("Employee Id to Delete  : "))
	if myemp == 0:
		break
	sqlstr="delete from newtable where emp_id= "+str(myemp)
	print(sqlstr)
	dbname=connstring="PyX1901.db"
	print()
	conn = sqlite3.connect(connstring)
	print(f'Connecting to the database ... {dbname} connected')
	cur=conn.cursor()
	try:
		cur.execute(sqlstr)
		print('Executing Query on database ... done')
	except (Exception, sqlite3.DatabaseError) as error:
		print("Error Executing Insert Query or Record Already Exists .... ")
		print(error)
	try:
		rows=cur.fetchall()
		print('Collecting results ... Output is ...')
		print(list(rows))
	except:
		print(" 1 Row(s) affected .....")
cur.close()
conn.commit()
print("End of Session ....")