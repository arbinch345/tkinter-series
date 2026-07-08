# label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()
window.geometry('500x400')

photo = PhotoImage(file='Images/butterfly.png')

label = Label(window, 
              text='Butterfly',
              bg='#00FF00',
              fg='black',
              font=('Arial', 20, 'bold'),
              relief=SUNKEN,          # boarder name
              bd=10,
              padx=20,
              pady=0,
              image=photo,
              compound='bottom')
label.pack()
# label.place(x=0,y=0)

window.mainloop()