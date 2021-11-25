from tkinter import *
class ListB:
    def __init__(self, root):
        self.f=Frame(root, height=700, width=800, cursor='pencil')
        self.f.propagate(0)
        self.f.pack()
        self.font=('Times', 18,'bold')

        self.l1=Label(text="Select toppings for your pizza ", font=self.font)
        self.l1.place(x=50, y=50)
        
        self.l2=Listbox(self.f, height=8, selectmode=MULTIPLE, activestyle='dotbox', font=self.font, fg='green', bg='yellow')
        self.l2.place(x=50, y=100)
        self.lst=['\nTomatoes', '\nOnions', '\nCapsicum', '\nPaneer', '\nMushroom', '\nBell Pepper', '\nMixed Herbs', '\nOlives']
        for i in self.lst:
            self.l2.insert(END, i)
        self.l2.bind('<<ListboxSelect>>', self.disp)

        self.t=Text(root, width=40, height=6, fg='grey', bg='white', wrap=WORD, font=self.font)
        self.t.place(x=300, y=100)
        self.t.insert(CURRENT, 'Your Pizza toppings are :')
                
    def disp(self,event):
        self.lst1=[]
        self.t.delete('1.25', END)
        ind=self.l2.curselection()
        for i in ind:
            self.t.insert(END,self.l2.get(i))
                
root=Tk()
sp=ListB(root)
root.mainloop()
