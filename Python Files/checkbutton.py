from tkinter import *
class CB:
    def __init__(self, root):
        self.f=Frame(root, height=550, width=800)
        self.f.propagate(0)
        self.f.pack()
        self.font=('Calibri', 24, 'bold')

        self.cb1v=IntVar()
        self.cb1=Checkbutton(self.f, text='python', command=self.check, variable=self.cb1v, fg="black", bg='white', font=self.font)
        self.cb1.grid(row=1, column=0)

        self.cb2v=IntVar()
        self.cb2=Checkbutton(self.f, text='   at   ', command=self.check, variable=self.cb2v, fg="black", bg='white', font=self.font)
        self.cb2.grid(row=2, column=0)

        self.cb3v=IntVar()
        self.cb3=Checkbutton(self.f, text='   os   ', command=self.check, variable=self.cb3v, fg="black", bg='white', font=self.font)
        self.cb3.grid(row=3, column=0)

        self.t=Text(root, width=20, height=5, fg='grey', bg='white', wrap=NONE, font=self.font)
        self.t.pack(side=RIGHT, padx=15, pady=15)
        
    def check(self):
        self.l=[self.cb1v.get(), self.cb2v.get(), self.cb3v.get()]
        print(self.l)
        self.s=["Python","Atomata Theory" , "Operating System"]
        self.t.delete('1.0', END)
        if 1 in self.l:
            self.t.insert(CURRENT, "You have selected :\n")
        for i in range(len(self.l)):
            if self.l[i]:
                self.t.insert(CURRENT,self.s[i]+"\n")
        
root=Tk()
cb=CB(root)
root.mainloop()
