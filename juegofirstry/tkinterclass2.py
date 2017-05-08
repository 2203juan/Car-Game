import tkinter
import time
import random

v= tkinter.Tk()
i=0
v.geometry("900x600")



def RunnerMovimiento():

      global canvas,p,i

      if i<500:
            canvas.move(p, 2,0)
            time.sleep(0.01)
            i=i+1
            v.after(3, RunnerMovimiento)

      elif i>=500 and i>0 :
            canvas.move(p, -2,0)
            time.sleep(0.01)
            i=i+1
            v.after(3, RunnerMovimiento)

canvas =tkinter.Canvas(v, width=1200, height=1000)
canvas.pack()
U=tkinter.PhotoImage(file="RedCar.png")
p=canvas.create_image(v,1200,1000,image=U)

RunnerMovimiento()
v.mainloop()





