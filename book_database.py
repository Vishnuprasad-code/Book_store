from tkinter import *
from backend import *

def view_all():
    list1.delete(0,END)
    for row in view():
        list1.insert(END,row)
def search_btn():
    list1.delete(0,END)
    for row in search(title_value.get(),author_value.get(),year_value.get(),ISBN_value.get()):
        list1.insert(END,row)
def add():
    list1.delete(0,END)
    insert(title_value.get(),author_value.get(),year_value.get(),ISBN_value.get())
    list1.insert(END,(title_value.get(),author_value.get(),year_value.get(),ISBN_value.get()))
def get_row(event):
    try:
        global sel_row
        index=list1.curselection()[0]
        sel_row=list1.get(index)

        e1.delete(0,END)
        e1.insert(END,sel_row[1])
        e2.delete(0,END)
        e2.insert(END,sel_row[2])
        e3.delete(0,END)
        e3.insert(END,sel_row[3])    
        e4.delete(0,END)
        e4.insert(END,sel_row[4])   
    except:
        pass 

def delete_btn():
    delete(sel_row[0],)   
    view_all()

def update_btn():
    update(sel_row[0],title_value.get(),author_value.get(),year_value.get(),ISBN_value.get())   
    view_all()    


window=Tk()

window.title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_value=StringVar()
e1=Entry(window,textvariable=title_value)
e1.grid(row=0,column=1)
author_value=StringVar()
e2=Entry(window,textvariable=author_value)
e2.grid(row=0,column=3)
year_value=StringVar()
e3=Entry(window,textvariable=year_value)
e3.grid(row=1,column=1)
ISBN_value=StringVar()
e4=Entry(window,textvariable=ISBN_value)
e4.grid(row=1,column=3)

list1=Listbox(window,height=10,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

sb2=Scrollbar(window, orient="horizontal")
sb2.grid(row=8,column=0,columnspan=2)

list1.bind("<<ListboxSelect>>",get_row)

list1.configure(yscrollcommand=sb1.set, xscrollcommand=sb2.set)
sb1.configure(command=list1.yview)
sb2.configure(command=list1.xview)

b1=Button(window,text="View All",width=12,command=view_all)
b1.grid(row=2,column=3)
b2=Button(window,text="Search",width=12,command=search_btn)
b2.grid(row=3,column=3)
b3=Button(window,text="Add",width=12,command=add)
b3.grid(row=4,column=3)
b4=Button(window,text="Update",width=12,command=update_btn)
b4.grid(row=5,column=3)
b5=Button(window,text="Delete",width=12,command=delete_btn)
b5.grid(row=6,column=3)
b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

connect()
view_all()

window.mainloop()
