from tkinter import *
class RB:
    def __init__(self, root):
        self.f=Frame(root, height=300, width=500)
        self.f.propagate(0)
        self.f.pack()
        self.font=('Calibri', 24, 'bold')
        self.t1=Text(root, width=50, height=2, fg='blue', bg='white', wrap=WORD, font=self.font)
        self.t1.pack(fill=X,side=TOP, padx=15, pady=15)
        self.t1.insert(CURRENT, "Which widget in python allows user to select only one option?")
        self.t = Text(root, width=50, height=2, fg='blue', bg='white', wrap=WORD, font=self.font)
        self.t.pack(fill=X, side=BOTTOM, padx=15, pady=15)
        self.t.insert(CURRENT, "")
        
        self.rbv=IntVar()
        
        self.rb1=Radiobutton(self.f, text='CheckButton', command=self.check, variable=self.rbv, value=1, fg="black", bg='white', font=self.font)
        self.rb1.grid(row=0, column=2)

        self.rb2=Radiobutton(self.f, text='RadioButton', command=self.check, variable=self.rbv, value=2, fg="black", bg='white', font=self.font)
        self.rb2.grid(row=1, column=2)

        self.rb3=Radiobutton(self.f, text='Text', command=self.check, variable=self.rbv, value=3, fg="black", bg='white', font=self.font)
        self.rb3.grid(row=2, column=2)

        
    def check(self):
        self.t.delete('1.0', END)
        #self.t.tag_add('ans','1.0', END)
        if self.rbv.get()==2:
            self.t.insert(END, "You have selected CORRECT option!!! :-D")
            #self.t.tag_configure('ans',foreground='green')
        else:
            self.t.insert(END, "You have selected incorrect option :-( ")
            #self.t.tag_configure('ans', foreground='red')
        
root=Tk()
rb=RB(root)
root.mainloop()
