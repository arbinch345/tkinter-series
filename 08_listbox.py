# listbox = a listening of selectable text items within it's own container

from tkinter import *

def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)
    # print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

window = Tk()
window.geometry("600x400")

listbox = Listbox(window,
                  font=('#f7ffde', 12),
                  fg='black',
                  bg="#7851B9",
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, 'pizza')
listbox.insert(1, 'pasta')
listbox.insert(1, 'salad')
listbox.insert(1, 'soup')
listbox.insert(1, 'burger')

listbox.config(height=listbox.size())                     # use when you have to change anything. here adjust height.

entrybox = Entry(window)
entrybox.pack()

submit_btn = Button(window,
                    text='submit',
                    command=submit)
submit_btn.pack()

add_btn = Button(window,
                 text='add',
                 command=add)
add_btn.pack()

delete_btn = Button(window,
                    text='delete',
                    command=delete)
delete_btn.pack()

window.mainloop()