import sqlite3
#import pwd
#dbname='db5'
#user='postgres'
#host='localhost'

dbname=connstring="PyX1901.db"
print()
conn = sqlite3.connect(connstring)
print(f'Connecting to the database ... {dbname} connected')
cur=conn.cursor()
sqlstr="""select * from newtable order by emp_id"""
try:
    cur.execute(sqlstr)
    print('Executing Query on database ... done')
except:
    print("Error Executing Select Query or Table does not exist .... ")
try:
    rows=cur.fetchall()
    print('Collecting results ... Output is ...')
    for i in range(len(rows)):
#       print(rows[i])
        print("%4d  %15s  %15s  %4d  %8.2f"
             %(rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4]))
except:
    print(" 00 Rows affected .....")
cur.close()


