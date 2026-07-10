from tkinter import *
from tkinter import filedialog


def save():
    file_path = filedialog.asksaveasfilename(
        initialdir=".",
        defaultextension='.txt',
        filetypes=[("Text file", "*.txt"),
                   ("HTML file", "*.html"),
                   ("All files", "*.*")]
    )

    if not file_path:
        return

    file_txt = text.get("1.0", END)
    with open(file_path, "w") as file:
        file.write(file_txt)


window = Tk()
window.geometry("700x500")

save_btn = Button(window,
                  text='save',
                  command=save)
save_btn.pack()

text = Text(window,
            font=('Ink Free', 14),
            fg='#111111',
            bg="#DFEADF")
text.pack()

window.mainloop()