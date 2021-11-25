import sqlite3

#import pwd
#dbname='db5'
#user='postgres'
#host='localhost'
#connstring="dbname="+dbname+" user="+user+" host="+host+" password="+pwd.password
dbname=connstring="PyX1901.db"
print()
conn = sqlite3.connect(connstring)
print(f'Connecting to the database ... {dbname} connected')
cur=conn.cursor()
sqlstr="""create table newtable (emp_id int, fname varchar(15), \
         lname varchar(15),  \
         deptno int, salary float ) """
try:
    cur.execute(sqlstr)
    print('Executing Query on database ... done')
except:
    print("Error Executing Create Table or Table Already Exists .... ")
try:
    rows=cur.fetchall()
    print('Collecting results ... Output is ...')
    print(list(rows))
except:
    print(" 0 Rows affected .....")
cur.close()
conn.commit()

