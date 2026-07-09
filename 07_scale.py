from tkinter import *

def submit():
    print(f"The temperature is {str(scale.get())} °C. ")

window = Tk()

hotImage = PhotoImage(file='Images/hot.png')
hotLabel = Label(window, image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              orient=VERTICAL,        # orientation of scale
              font=('Consolas', 20),
              tickinterval=10,          # adds numeric indicators for value
              showvalue=0,              # hides current value
              resolution=10,             # increment of slider
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111')

scale.set(50)
# scale.set(((scale['from']-scale['to'])/2)+scale['to'])   # set the current value of slider
scale.pack()

coldImage = PhotoImage(file='Images/cold.png')
coldLabel = Label(window, image=coldImage)
coldLabel.pack()

scale_btn = Button(window,
                   text='submit',
                   font=('Arial', 15),
                   padx=0,
                   pady=0,
                   command=submit)
scale_btn.pack()

window.mainloop()