""" this program has book information
    title, author name
    year,rating
    view
    search
    add
    update
    delete
    close
"""
from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END,selected_tuple[4])
def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),rating_text.get())

def view_command():
    list1.delete(0,END)
    for rows in backend.view():
        list1.insert(END,rows)
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),rating_text.get()):
        list1.insert(END,row)
def add_command():

        backend.insert(title_text.get(),author_text.get(),year_text.get(),rating_text.get())
        list1.delete(0, END)
        list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),rating_text.get()))



window = Tk()
window.wm_title("bookstore")

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author name")
l2.grid(row=0,column=3)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="Rating")
l4.grid(row=1,column=3)

title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0,column=4)

year_text = StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

rating_text = StringVar()
e4 = Entry(window,textvariable=rating_text)
e4.grid(row=1,column=4)

list1 = Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)


sb1 = Scrollbar(window)
sb1.grid(row=2,column=3,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind("<<ListboxSelect>>",get_selected_row)

b1 = Button(window,text="Viewall",width=12,command=view_command)
b1.grid(row=2,column=4)

b2 = Button(window,text="search",width=12,command=search_command)
b2.grid(row=3,column=4)

b3 = Button(window,text="add entry",width=12,command=add_command)
b3.grid(row=4, column=4)

b4 = Button(window,text="update",width=12,command=update_command)
b4.grid(row=5, column=4)

b1 = Button(window,text="delete",width=12,command=delete_command)
b1.grid(row=6, column=4)

b1 = Button(window,text="close",width=12,command=window.destroy)
b1.grid(row=7, column=4)
window.mainloop()
