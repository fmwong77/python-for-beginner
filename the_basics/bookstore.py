from tkinter import *
from bookstore_backend import Database

database = Database("books.db")

def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)

    for row in database.search(title_text.get(), author_text.get()):
        list1.insert(END, row)

def update_command():
    database.update(selected_tuple[0], e1.get())
    view_command()

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def getSelected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]

        selected_tuple = list1.get(index)

        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])

        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])

        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])

        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

window = Tk()

window.wm_title("Book Store")
label1 = Label(window, text="Title")
label1.grid(row=0, column=0)

label2 = Label(window, text="Author")
label2.grid(row=0, column=2)

label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
list1.bind('<<ListboxSelect>>', getSelected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

btn1 = Button(window, text="View All", width=12, command=view_command)
btn1.grid(row=2, column=3)

btn2 = Button(window, text="Search Entry", width=12, command=search_command)
btn2.grid(row=3, column=3)

btn3 = Button(window, text="Add Entry", width=12, command=add_command)
btn3.grid(row=4, column=3)

btn4 = Button(window, text="Update Selected", width=12, command=update_command)
btn4.grid(row=5, column=3)

btn5 = Button(window, text="Delete Selected", width=12, command=delete_command)
btn5.grid(row=6, column=3)

btn6 = Button(window, text="Close", width=12)
btn6.grid(row=7, column=3)

window.mainloop()