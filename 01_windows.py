# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

from tkinter import *

window = Tk()    # instantiate an instance of a window

window.geometry("700x600")
window.title("First GUI Program")

icon = PhotoImage(file='Images/instagram.png')   # only accepts png format 
window.iconphoto(True, icon)
window.config(bg='#5cfcff')

window.mainloop()  # place window on computer screen. listen for window