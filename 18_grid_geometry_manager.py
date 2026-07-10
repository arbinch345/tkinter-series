# grid() = geometry manager that organizes widgets in a table-like structure in a parent

from tkinter import *

window = Tk()
window.geometry('300x200')

titleLabel = Label(window, text='Enter your info', font=('Arial', 18))
titleLabel.grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text='First Name: ', width=15).grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window, text='Last Name: ').grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window, text='Email: ').grid(row=3, column=0)
emailEntry = Entry(window).grid(row=3, column=1)

submit_btn = Button(window, text='submit').grid(row=4, column=0, columnspan=2)

window.mainloop()