from tkinter import *

class MyButton:
    def __init__(self,root):
        self.f=Frame(root, height=400, width=500)
        self.f.propagate(0)
        self.f.pack()
        self.m=Message(self.f, text="Here one can enter more than one line of text.", font= ('Calibri', 18, 'bold'), fg='red')
        self.m.pack(side=LEFT, fill=Y)

root=Tk()
my=MyButton(root)
root.mainloop()
