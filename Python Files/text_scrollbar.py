from tkinter import *

class MyText:
    def __init__(self,root):
        self.t=Text(root, width=20, height=8, font=("Verdana", 15), fg="red", bg='yellow', wrap=WORD)
        self.t.insert(END, "this is how text widget works.\nlets go on a new line\n this is the third line.")
        self.t.pack(side=LEFT)
        #insert(END/ CURRENT)

        self.img=PhotoImage(file='gorilla.gif')
        self.t.image_create(END, image=self.img)

        self.t.tag_add("tag1", '1.5', '2.2')
        self.t.tag_config('tag1', background='wheat', foreground='blue', font=('Calibri', 20, 'italic'))
        
        self.s=Scrollbar(root, orient=VERTICAL, command=self.t.yview)
        #orient=VERTICAL/ HORIZONTAL --> scroll bar is vertical or horizontal
        #yview/ xview --> scrolling
        self.t.configure(yscrollcommand=self.s.set)
        #attaches the scroll bar to text
        self.s.pack(side=RIGHT, fill=Y)

root=Tk()
my=MyText(root)
root.mainloop()
