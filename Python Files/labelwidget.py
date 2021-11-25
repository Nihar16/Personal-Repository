from tkinter import *

class MyButton:
    def __init__(self):
        self.f=Frame(root, height=400, width=500)
        self.f.propagate(0)
        self.f.pack()
        self.b1=Button(self.f, text='Click Here', width=15, height=2, command=self.buttonClick, bg='yellow', fg='green')
        self.b2=Button(self.f, text='Close', width=15, height=2, command=root.destroy, bg='yellow', fg='green')
        self.b1.grid(row=1, column=1)
        self.b2.grid(row=1, column=3)
        '''self.b1.pack(side=LEFT)
        self.b2.pack(side=RIGHT)'''


    def buttonClick(self):
        self.fnt=('Calibri', 18, 'bold')
        self.l=Label(self.f, text="Thank you !! You may close now", width=25, height=2, font=self.fnt, fg='red')
        self.l.grid(row=2, column=2)

root=Tk()
my=MyButton()
root.mainloop()
