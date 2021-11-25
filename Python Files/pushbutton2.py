from tkinter import *

class MyButton:
    def __init__(self):
        self.f=Frame(root, height=400, width=500)
        self.f.propagate(1)
        self.f.pack()
        self.b=Button(self.f, text='Click Here', width=15, height=2, command=self.buttonClick, bg='yellow', fg='green', activebackground='blue', activeforeground='red')
        self.b.pack()        


    def buttonClick(self):
        print("Clicked!")

root=Tk()
my=MyButton()
root.mainloop()
