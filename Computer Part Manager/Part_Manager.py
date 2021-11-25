from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Feilds', 'Please include all Feilds')
        return
    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    try:
        global select_item
        index = parts_list.curselection()
        select_item = parts_list.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, select_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, select_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, select_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, select_item[4])
    except IndexError:
        pass

def remove_item():
    db.remove(select_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(select_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    populate_list()

def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)

#Create Window Object
app = Tk()

#Parts
part_text = StringVar()
part_label = Label(app,text='Part Name', font=('bold',14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

#Customer
customer_text = StringVar()
customer_label = Label(app,text='Customer Name', font=('bold',14), pady=20)
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

#Retailer
retailer_text = StringVar()
retailer_label = Label(app,text='Retailer', font=('bold',14), pady=20)
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

#Price
price_text = StringVar()
price_label = Label(app,text='Price', font=('bold',14), pady=20)
price_label.grid(row=1, column=2,sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

#Parts List (Listbox)
parts_list = Listbox(app, height=10, width=60, border=1)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#Create Scrollbar
Scrollbar = Scrollbar(app)
Scrollbar.grid(row=5, column=3)

#Set Scrollbar to List
parts_list.configure(yscrollcommand=Scrollbar.set)
Scrollbar.configure(command=parts_list.yview)

#Bind Select
parts_list.bind('<<ListboxSelect>>', select_item)

#Buttons

#<---Add--->
add_btn = Button(app, text='Add Part', width=10, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

#<---Remove--->
remove_btn = Button(app, text='Remove Part', width=10, command=remove_item)
remove_btn.grid(row=2, column=1)

#<---Update--->
update_btn = Button(app, text='Update Part', width=10, command=update_item)
update_btn.grid(row=2, column=2)

#<---Clear--->
clear_btn = Button(app, text='Clear Input', width=10, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('Computer Part Manager')
app.geometry('700x400')

#Populate List
populate_list()

#Start Program
app.mainloop() 