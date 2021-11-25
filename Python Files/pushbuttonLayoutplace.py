from tkinter import *

class MyButton:
    def __init__(self):
        self.f=Frame(root, height=400, width=500,bg='black')
        self.f.propagate(0)
        self.f.pack()
        self.b1=Button(self.f, text='Red', command=lambda: self.buttonClick(1), width=15, height=2)
        self.b2=Button(self.f, text='Green', command=lambda: self.buttonClick(2), width=15, height=2)
        self.b3=Button(self.f, text='Yellow', command=lambda: self.buttonClick(3), width=15, height=2)
        self.b1.place(x=20, y=20, width = 50, height= 50)
        self.b2.place(x= 20, y= 100, width = 50, height= 50)
        self.b3.place(x=100, y=100, width = 50, height= 50)


    def buttonClick(self,id):
        if id==1:
            self.f["bg"]="red"
        elif id==2:
            self.f["bg"]="green"
        else:
            self.f["bg"]="yellow"

root=Tk()
my=MyButton()
root.mainloop()
