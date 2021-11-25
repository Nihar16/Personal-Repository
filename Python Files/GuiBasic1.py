from tkinter import *
root=Tk()

root.title("1st Window")
root.geometry("800x1200+200+100")
#root.mainloop()


c=Canvas(root,bg="wheat",height=800,width=1200)

c.pack()

c.create_line(50,50,100,100,150,50, width=2, fill="blue",activefill="red")

c.create_oval(50,100,150,200,width=2,fill="red", outline="green", activefill="plum")

c.create_rectangle(50,200,150,350,width=2,fill="DodgerBlue2", outline="black", activefill="yellow")

c.create_polygon(25,350,175,350,175,550,100,450,25,550,width=2,fill="orange", activefill="cyan",smooth=1,outline='magenta')

c.create_arc(75,125,125,175,start=210,extent=120, outline='HotPink4',width=2,style='chord', fill='ivory', activefill="purple")

f=("Helvetica",20,'bold italic underline')
c.create_text(100,275,font=f, text='WOW', fill='yellow', activefill='IndianRed2')

file1=PhotoImage(file="Enter your file")
file2=PhotoImage(file="Enter your file")
c.create_image(450,300,anchor=CENTER, image=file1,activeimage=file2)

root.mainloop()
