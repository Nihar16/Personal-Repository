import MySQLdb
from tkinter import *
from sqlpwd import pwd

r=Tk()
r.title("Student Details")
r.geometry('600x400+100+100')
fnt=('Times', 18)

def getdata(rn):
    conn=MySQLdb.connect(host='localhost', database='world', user='root', password=pwd)
    cursor=conn.cursor()
    
    query="select * from StudentDetails where RollNo='%d'"
    tup=(int(rn))
    cursor.execute(query % tup)
    datafetch=cursor.fetchone()
    
    conn.commit()
    conn.close()
    return datafetch

def display(self):
    data=e1.get()
    l1=Label(r, text='Fetching Details for Roll No. '+data, font=fnt)
    l1.place(x=50,y=100)

    dataret=getdata(data)
    colname=('Roll No.', 'Name', 'Age', 'Sex', 'Branch', 'Marks')
    formstr=''
    for i in range(len(dataret)):
        formstr=formstr+colname[i]+"\t"+str(dataret[i])+"\n"
    
    l2=Label(r, text=formstr, font=fnt, justify=LEFT)
    l2.place(x=50,y=150)


l1=Label(r, text='Enter Roll Number', font=fnt)
l1.place(x=50,y=50)

e1=Entry(r, width=8, fg='grey10', bg='grey100', font=fnt)
e1.bind('<Return>', display)
e1.place(x=275,y=50)

r.mainloop()
