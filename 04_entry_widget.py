# entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print("Hello " + username)
    # entry.config(state=DISABLED) # Disable the text when it is submitted!

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()
window.geometry('600x200')

entry = Entry(window,
              font=('Arial', 25),
              fg='black',
              bg="white",
              show='*')       # show "*" when you type but the text is shown after submission in terminal
# entry.insert(0, 'Enter anything')   # Already appear in the box
entry.pack(side=LEFT, padx=10, pady=0)

submit_btn = Button(window, text='submit', command=submit)
submit_btn.pack(side=RIGHT, padx=5, pady=5)
# submit_btn.place(x=0, y=0)

delete_btn = Button(window, text='delete', command=delete)
delete_btn.pack(side=RIGHT, padx=5, pady=5)

backspace_btn = Button(window, text='backspace', command=backspace)
backspace_btn.pack(side=RIGHT, padx=5, pady=5)

window.mainloop()