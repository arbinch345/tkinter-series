# button = you click it, then it does stuff

from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(f"You clicked the button {count} times!")
    # print(count)

window = Tk()
window.geometry('500x400')

photo = PhotoImage(file='Images/likee.png')

button = Button(window,
                text='click me',
                command=click,
                # command=window.destroy,          # shutdown the window
                font=('Comic Sans', 25),
                fg='#00FF00',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black',
                # state=DISABLED,
                state=ACTIVE,
                image=photo,
                compound='left')           # can't click
button.pack()


window.mainloop()