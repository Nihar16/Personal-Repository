"""3 push buttons that change the background colour
    to pass argument to the event handler method, use lambda expression
    command=lambda: buttonClick(arguments)
"""
from tkinter import *

class MyButton:
    def __init__(self):
        self.f=Frame(root, height=400, width=500,bg='black')
        self.f.propagate(0)
        self.f.pack()
        self.b1=Button(self.f, text='Red', command= lambda: self.buttonClick(1), width=15, height=2)
        self.b1.pack()
        self.b2=Button(self.f, text='Green', command=lambda: self.buttonClick(2), width=15, height=2)
        self.b2.pack()
        self.b3=Button(self.f, text='Yellow', command=lambda: self.buttonClick(3), width=15, height=2)
        self.b3.pack()


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
