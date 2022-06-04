from tkinter import *
from tkinter.ttk import*
from time import strftime

root = Tk()
root.title("Horloge")

def time():
    string = StringVar()
    string = strftime('%H:%M ')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font =('calibiri',40,'bold'),background = 'blue', foreground = 'white')
lbl.pack(anchor = 'center')
time()

mainloop()

