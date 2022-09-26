from tkinter import *
from tkinter import ttk

root = Tk()

root.attributes('-transparentcolor','#f0f0f0')

canvas = Canvas(root, width=450, height=600)
canvas.pack()

img = PhotoImage(file=".images/Lorem.png")

canvas.create_image(0,0,anchor=NW, image=img)

root.mainloop()