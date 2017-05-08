from tkinter import*
import time
import random

v= Tk()
i=0
v.config(bg="black")
v.geometry("1800x600")

canvas =Canvas(v, width=900, height=900)

u=PhotoImage(file="BlueCar.png")
p=canvas.create_image(50+i,60+i, image=u)


"""
def RunnerMovimiento():

      global canvas,p,i,u
      
      for i in range(3,9):
"""
            #if i<=390 :
canvas.move(p, 2,0)
time.sleep(0.001)


                

  #          if i==390  :
time.sleep(0.001)


                  
          
     
    

     

canvas.pack()


v.mainloop()





