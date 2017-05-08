import tkinter
import time 

v = tkinter.Tk()

m= 0


def movimiento():
    """
    """
    global v,canvas,p,m
    if(m<500):
        canvas.move(p,0,2)
        time.sleep(0.02)
    
        m = m+ 1
        v.after(5,movimiento)
            
   
        

canvas = tkinter.Canvas(v,width=900,height=600)
canvas.pack()
vancar=tkinter.PhotoImage(file="RedCar.png")
p = canvas.create_image(50,50,image=vancar)

movimiento()

v.mainloop()
