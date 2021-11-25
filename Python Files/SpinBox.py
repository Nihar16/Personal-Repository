from tkinter import *
class Spin:
    def __init__(self, root):
        self.f=Frame(root, height=700, width=800, cursor='pencil')
        self.f.propagate(0)
        self.f.pack()
        self.font=('Helvetica', 18,'bold')

        self.l1=Label(text="Enter your Name : ", font=self.font)
        self.l1.place(x=50, y=50)
        self.l2=Label(text="Select your qualification : ", font=self.font)
        self.l2.place(x=50, y=100)
        self.l3=Label(text="Select the applicable post : ", font=self.font)
        self.l3.place(x=50, y=150)

        self.e1=Entry(self.f, fg='black', bg='grey90',width=15, font=self.font)
        self.e1.place(x=380, y=50)
        
        self.int1=IntVar()
        self.sp1=Spinbox(self.f, from_=10, to=20, textvariable=self.int1, fg='black', bg='grey90',width=5, font=self.font)
        self.sp1.place(x=380, y=100)
        
        self.str1=StringVar()
        self.strlist=['Lecturer', 'Assistant Professor', 'Associate Professor', 'Profesor','Head of Department']
        self.sp2=Spinbox(self.f, values=self.strlist, textvariable=self.str1, fg='black', bg='grey90',width=15, font=self.font)
        self.sp2.place(x=380, y=150)

        self.b=Button(self.f, text='Apply', font=self.font, command=self.disp)
        self.b.place(x=100, y= 200)

    def disp(self):
        self.l6=Label(text='Hello '+self.e1.get(), font=self.font)
        self.l6.place(x=50, y= 250)
        self.l4=Label(text='Your Highest qualification is'+str(self.int1.get()) + " class", font=self.font)
        self.l4.place(x=50, y= 300)
        self.l5=Label(text='You have applied for the post of '+self.str1.get(), font=self.font)
        self.l5.place(x=50, y= 350)
        
root=Tk()
sp=Spin(root)
root.mainloop()
