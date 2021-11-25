from tkinter import *

def buttonClick():
    print("Clicked!")

root=Tk()

f=Frame(root, height=400, width=500)
f.propagate(0)
#f.propagate(1)
f.pack()

b=Button(f, text='Click Here', width=15, height=2, bg='yellow', fg='green', activebackground='blue', activeforeground='red')

#b.bind('<Button-1>',buttonClick)
#b.bind('<Button-3>',buttonClick)
#b.bind('<Enter>',buttonClick)

#b=Button(f, text='Click Here', width=15, height=2, command=buttonClick, bg='yellow', fg='green', activebackground='blue', activeforeground='red')
b.pack()
root.mainloop()
