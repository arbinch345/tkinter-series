# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window, bg='#00FF00', bd=5, relief=SUNKEN)
frame.place(x=0, y=0)

button = Button(frame, text='W', font=('Consolas', 25), width=3).pack(side=TOP)
button = Button(frame, text='A', font=('Consolas', 25), width=3).pack(side=LEFT)
button = Button(frame, text='S', font=('Consolas', 25), width=3).pack(side=LEFT)
button = Button(frame, text='D', font=('Consolas', 25), width=3).pack(side=LEFT)

# button = Button(window, text='W', font=('Consolas', 25), width=3).pack(side=TOP)
# button = Button(window, text='A', font=('Consolas', 25), width=3).pack(side=LEFT)
# button = Button(window, text='S', font=('Consolas', 25), width=3).pack(side=LEFT)
# button = Button(window, text='D', font=('Consolas', 25), width=3).pack(side=LEFT)

window.mainloop()