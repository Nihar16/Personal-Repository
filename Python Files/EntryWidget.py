from tkinter import *
class Login:
    def __init__(self, root):
        self.f=Frame(root, height=350, width=800, cursor='pencil')
        self.f.propagate(0)
        self.f.pack()
        self.font=('Arial', 20,'bold')

        self.l1=Label(text="Enter your Username : ", font=self.font)
        self.l1.place(x=50, y=50)
        self.l2=Label(text="Enter your Password : ", font=self.font)
        self.l2.place(x=50, y=100)

        self.e1=Entry(self.f, fg='black', bg='grey90',width=15, font=self.font)
        self.e1.place(x=380, y=50)
        self.e2=Entry(self.f, fg='black', bg='grey90',width=15, font=self.font, show='*')
        self.e2.bind("<Return>",self.disp)
        self.e2.place(x=380, y=100)
        
    def disp(self, event):
        s1=self.e1.get()
        s2=self.e2.get()

        self.l3=Label(text="Thank you for logging in "+s1, font=self.font)
        self.l3.place(x=150, y=150)

root=Tk()
en=Login(root)
root.mainloop()
