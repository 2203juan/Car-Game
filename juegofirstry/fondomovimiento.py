import tkinter
import time

v=tkinter.Tk()
v.geometry("1890x1000")
canvas=tkinter.Canvas(v, width=1350, height=700,bd=0,highlightthickness=0)

x=tkinter.PhotoImage(file="TryFont.png")

y= canvas.create_image(850,300, image=x)

canvas.move(y,0,5)
canvas.focus_set()
canvas.pack()

v.mainloop()
