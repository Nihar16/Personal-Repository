from tkinter import *
class MenuB:
    def __init__(self, root):
        self.font=('Times', 18,'bold')

        self.menubar=Menu(root)
        root.config(menu=self.menubar)

        self.breadmenu=Menu(root, tearoff=1)
        self.breadmenu.add_command(label='Parmesan Oregano' , command=self.ok)
        self.breadmenu.add_command(label='Multi Grain' , command=self.ok)
        self.breadmenu.add_command(label='Italian' , command=self.ok)
        self.breadmenu.add_separator()
        self.menubar.add_cascade(label='Breads', menu=self.breadmenu)

        self.veggiemenu=Menu(root, tearoff=0)
        self.veggiemenu.add_command(label='Cucumber' , command=self.ok)
        self.veggiemenu.add_command(label='Bell Pepper' , command=self.ok)
        self.veggiemenu.add_command(label='Lettuce' , command=self.ok)
        self.veggiemenu.add_command(label='Tomatoes' , command=self.ok)
        self.veggiemenu.add_command(label='Onions' , command=self.ok)
        self.veggiemenu.add_command(label='Patty' , command=self.ok)
        self.veggiemenu.add_separator()
        self.menubar.add_cascade(label='Veggies', menu=self.veggiemenu)

        self.final=Menu(root, tearoff=1)
        self.final.add_command(label='Finish' , command=root.destroy)
        self.menubar.add_cascade(label='Next', menu=self.final)
        
    def ok(self):
        pass
                
root=Tk()
root.title("Make you Own Subway Sandwich")
sp=MenuB(root)
root.mainloop()
