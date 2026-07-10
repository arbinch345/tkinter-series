from tkinter import *

def create_window():
    new_window = Tk()         # creates new window
                              # Tk() = new independent window

    # window.destroy()          # closes old window

window = Tk()
window.geometry('300x200')

Button(window, text='create new window', command=create_window).pack()

window.mainloop()


# from tkinter import *
# root = Tk()
# root.title('GfG')
# top = Toplevel()
# top.title('Python')
# top.mainloop()