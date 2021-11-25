from tkinter import *
class Spin:
    def __init__(self, root):
        self.f=Frame(root, height=1200, width=1200, cursor='pencil')
        self.f.propagate(0)
        self.f.pack()
        self.font=('Helvetica', 18,'bold')

        self.l1=Label(text="Enter your Name : ", font=self.font)
        self.l1.place(x=50, y=215)
        self.l2=Label(text="Select your qualification : ", font=self.font)
        self.l2.place(x=50, y=270)
        self.l3=Label(text="Select the applicable post : ", font=self.font)
        self.l3.place(x=50, y=320)

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
        self.b.place(x=900, y= 50)

    def disp(self):
        self.l6=Label(text='Hello '+self.e1.get(), font=self.font)
        self.l6.place(x=500, y= 360)
        self.l4=Label(text='Your Highest qualification is'+str(self.int1.get()) + " class", font=self.font)
        self.l4.place(x=500, y= 400)
        self.l5=Label(text='You have applied for the post of '+self.str1.get(), font=self.font)
        self.l5.place(x=500, y= 430)


class RB:
    def __init__(self, root):
        self.f=Frame(root, height=900, width=900)
        self.f.propagate(0)
        self.f.pack()
        self.font=('Calibri', 24, 'bold')
        self.t1=Text(root, width=50, height=2, fg='blue', bg='white', wrap=WORD, font=self.font)
        self.t1.pack(fill=X,side=BOTTOM, padx=5, pady=5)
        self.t1.insert(CURRENT, "Select Your Gender")
        self.t = Text(root, width=50, height=2, fg='blue', bg='white', wrap=WORD, font=self.font)
        self.t.pack(fill=X, side=BOTTOM, padx=5, pady=5)
        self.t.insert(CURRENT, "")
        
        self.rbv=IntVar()
        
        self.rb1=Radiobutton(self.f, text='Male', command=self.check, variable=self.rbv, value=1, fg="black", bg='white', font=self.font)
        self.rb1.grid(row=0, column=1)

        self.rb2=Radiobutton(self.f, text='Female', command=self.check, variable=self.rbv, value=2, fg="black", bg='white', font=self.font)
        self.rb2.grid(row=1, column=1)

        self.rb3=Radiobutton(self.f, text='Dont want to specify', command=self.check, variable=self.rbv, value=3, fg="black", bg='white', font=self.font)
        self.rb3.grid(row=2, column=1)

        
    def check(self):
        self.t.delete('1.0',END)
        #self.t.tag_add('ans','3.0', END)
        if self.rbv.get()==1:
            self.t.insert(END, "You have selected CORRECT option!!! :-D")
            #self.t.tag_configure('ans',foreground='green')
        elif self.rbv.get()==2:
            self.t.insert(END, "You have selected CORRECT option!!! :-D")
            #self.t.tag_configure('ans',foreground='green')
        else:
            self.t.insert(END, "You have selected incorrect option :-( ")
            #self.t.tag_configure('ans', foreground='red')


class MenuB:
    def __init__(self, root):
        self.font=('Times', 18,'bold')

        self.menubar=Menu(root)
        root.config(menu=self.menubar)

        self.accountmenu=Menu(root, tearoff=1)
        self.accountmenu.add_command(label='signup' , command=self.ok)
        self.accountmenu.add_command(label='My account ' , command=self.ok)
        self.accountmenu.add_command(label='Login' , command=self.ok)
        self.accountmenu.add_separator()
        self.menubar.add_cascade(label='account', menu=self.accountmenu)

        self.optionsmenu=Menu(root, tearoff=1)
        self.optionsmenu.add_command(label='new' , command=self.ok)
        self.optionsmenu.add_command(label='open' , command=self.ok)
        self.optionsmenu.add_command(label='save' , command=self.ok)
        self.optionsmenu.add_command(label='save-as' , command=self.ok)
        self.optionsmenu.add_command(label='print' , command=self.ok)
        self.optionsmenu.add_command(label='quit' , command=self.ok)
        self.optionsmenu.add_separator()
        self.menubar.add_cascade(label='options', menu=self.optionsmenu)

        self.final=Menu(root, tearoff=1)
        self.final.add_command(label='Finish' , command=root.destroy)
        self.menubar.add_cascade(label='Next', menu=self.final)
        
    def ok(self):
        pass
                

root=Tk()
rb=RB(root)
sp=Spin(root)
root.title("REGISTER")
sp=MenuB(root)

root.mainloop()