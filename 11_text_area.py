# text widget = functions like a text area, you can enter multiple lines of text

from tkinter import *

def submit():
    input = text.get('1.0', END)
    print(input)

window = Tk()

text = Text(window,
            font=('Ink Free', 14),
            bg='light yellow',
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg='black')

text.pack()

submit_btn = Button(window,
                    text='submit',
                    command=submit)
submit_btn.pack()

window.mainloop()