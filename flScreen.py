from tkinter import *
from tkinter import *
import time
root = Tk()
clock = Label(root, font=('calibri', 150, 'bold'),
            background='black',
            foreground='white')

clock.pack(fill=BOTH, expand=1)

def tick():
    s = time.strftime('%H:%M:%S %p')
    if s != clock["text"]:
        clock["text"] = s
    clock.after(200, tick)
tick()
root.mainloop()