# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if (x.get() == 0):
        print("You ordered pizza!")
    elif (x.get() == 1):
        print("You ordered Hamburger!")
    elif (x.get() == 2):
        print("You ordered hotdog!")
    else:
        print("huh!!!")

window = Tk()
window.geometry('250x200')

PizzaImage = PhotoImage(file='Images/pizza.png')
HamburgerImage = PhotoImage(file='Images/hamburger.png')
HotdogImage = PhotoImage(file='Images/hotdog.png')

FoodImages = [PizzaImage, HamburgerImage, HotdogImage]

x = IntVar()

for index in range(len(food)):
    radio_btn = Radiobutton(window, 
                            text=food[index],     # adds text to radio buttons
                            variable=x,           # groups radiobuttons together if they share the same variable
                            value=index,          # assigns each radiobutton a different value
                            padx=25,
                            font=("Impact", 15),
                            image=FoodImages[index],   # add photo 
                            compound='left',
                            # indicatoron=0,              # eliminates the circle
                            width=375,                  # sets width of radio button
                            command=order)              # set command of radiobutton to function
    radio_btn.pack(anchor=W)


window.mainloop()