import MySQLdb
from sqlpwd import pwd
conn=MySQLdb.connect(host='localhost', database='world', user='root', password=pwd)
cursor=conn.cursor()

#CREATE A TABLE
cursor.execute('drop table if exists StudentDetails')
query1='create table StudentDetails(RollNo int, Name char(20), Age int, Sex char(01), Branch char(4), Marks float)'
cursor.execute(query1)
print("Table created")

#ADD DATA
query2='insert into StudentDetails(RollNo,Name, Age, Sex, Branch, Marks) values(100, "Shri Deshpande", 16, "M", "INFT", 8.9)'
cursor.execute(query2)

tup1=(101,"Mehul Kalyan", 17, "M", "CMPN", 7.2)
query3='insert into StudentDetails(RollNo,Name, Age, Sex, Branch, Marks) values("%d", "%s", "%d", "%s", "%s", "%1.1f")'
cursor.execute(query3 % tup1)

tup1=(102,"Meena Pradosh", 20, "F", "INFT", 9.1)
cursor.execute(query3 % tup1)

tup1=(103,"Durga Singh", 18, "F", "EXTC", 7.7)
cursor.execute(query3 % tup1)

tup1=(104,"Sana Vaishya", 19, "F", "EXTC", 6.3)
cursor.execute(query3 % tup1)

tup1=(105,"Bharat Ratna", 21, "M", "INFT", 5.6)
cursor.execute(query3 % tup1)

conn.commit()
conn.close()
