from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='This is an info msg box', message='correct!', icon='info')         # you can use "error", " warning" and if not use (then default)
    # messagebox.showwarning(title='WARNING', message='You have a VIRUS!')
    # messagebox.showerror(title='ERROR', message='something went error!')

    # if messagebox.askokcancel(title="ask or cancel", message='Do you want to do?'):
    #     print('Yes! I want to do!')
    # else:
    #     print("You canceled it!")

    # if messagebox.askretrycancel(title="ask or cancel", message='Do you want to do?'):
    #     print('Yes! I want to retry!')
    # else:
    #     print("You canceled it!")

    # if messagebox.askyesno(title="Yes or No", message='Do you want like a cake?'):
    #     print('Yes! I want to retry!')
    # else:
    #     print("why not?")

    # answer = (messagebox.askquestion(title='ask question', message='Do you like pie?'))
    # if answer == 'yes':
    #     print("I like the pie too?")
    # else:
    #     print("Why do you not like pie?")

    answer = messagebox.askyesnocancel(title='yes no cancel', message='Do you like to code?')
    if answer == True:
        print("you like to code!")
    elif answer == False:
        print("why are you watching video on Youtube!")
    else:
        print("You have dodged the question!")

window = Tk()
window.geometry("300x200")

btn = Button(window,
             text='click me',
             command=click)
btn.pack()

window.mainloop()