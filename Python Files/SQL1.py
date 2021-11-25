import MySQLdb
from sqlpwd import pwd
conn=MySQLdb.connect(host='localhost', database='world', user='root', password=pwd)
cursor=conn.cursor()

#CREATE A TABLE
'''cursor.execute('drop table if exists StudentDetails')
query1='create table StudentDetails(RollNo int, Name char(20), Age int, Sex char(01), Branch char(4), Marks float)'
cursor.execute(query1)
print("Table created")


#ADD DATA
query2='insert into StudentDetails values(100, "Shri Deshpande", 16, "M", "INFT", 8.9)'
cursor.execute(query2)

tup1=(101,"Mehul Kalyan", 17, "M", "CMPN", 7.2)
query3='insert into StudentDetails values("%d", "%s", "%d", "%s", "%s", "%1.1f")'
cursor.execute(query3 % tup1)

n=int(input("Enter the no of students : "))
for i in range (n):
    rollNo=int(input("Enter the roll no of student "+str(i+1)+" : "))
    name=input("Enter the name of student "+str(i+1)+" : ")
    age=int(input("Enter the age of student "+str(i+1)+" : "))
    sex=input("Enter the sex of student "+str(i+1)+" (M/F): ")
    sex=sex.upper()
    branch=input("Enter the branch of student "+str(i+1)+" : ")
    branch=branch.upper()
    marks=float(input("Enter the sgpa of student "+str(i+1)+" : "))
    
    tup2=(rollNo, name, age, sex, branch, marks)
    query4='insert into StudentDetails(RollNo,Name, Age, Sex, Branch, Marks) values("%d", "%s", "%d", "%s", "%s", "%1.1f")'
    cursor.execute(query4 % tup2)
'''

#RETRIEVE ALL THE DETAILS
cursor.execute('select * from StudentDetails')
print("The first entry is :\n",cursor.fetchone())
print("Rest of the students are :\n",cursor.fetchall())

print()

#SELECTIVE RETRIEVAL
cursor.execute("select * from StudentDetails where Sex = 'F'")
data=cursor.fetchall()
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end='\t')
    print()
print()
#UPDATE DATA
cursor.execute("update StudentDetails  set Marks=8.9 where RollNo=103")
cursor.execute("select * from StudentDetails")
data=cursor.fetchall()
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end='\t')
    print()
print()
#DELETE DATA
cursor.execute("delete from StudentDetails where Age<18")
cursor.execute("select * from StudentDetails")
data=cursor.fetchall()
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end='\t')
    print()

conn.commit()
conn.close()
