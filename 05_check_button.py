from tkinter import *

def display():
    if (x.get() == 1):
        print("You agree!")
    else:
        print("You don't agree!")

window = Tk()
window.geometry("500x300")

x = IntVar()     # (you can use BooleanVar, change the onvalue=True, offvalue=False)

photo = PhotoImage(file='Images/instagram.png')   # you can insert image at the side of the checkpoint

check_btn = Checkbutton(window,
                        text="I agree to something",
                        variable=x,
                        onvalue=1,
                        offvalue=0,
                        command=display,
                        font=('Arial', 15),
                        bg="white",
                        fg="black",
                        activebackground="white",
                        activeforeground="black",
                        image=photo,
                        compound='left')
check_btn.pack()

window.mainloop()