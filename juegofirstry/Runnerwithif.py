import tkinter
import time

v = tkinter.Tk()

m= 0

def Runner():
    """
    """
    global canvas,p,m
    if(m>=0 and m<100):
       
        canvas.move(p,10,1)
        time.sleep(0.000001)

    
        m = m+ 1
        v.after(10,Runner)

    elif(m>=20):
         canvas.move(p,-10,1)
         time.sleep(0.000001)
         m = m+1
         v.after(10,Runner)

    if m>200:
         canvas.move(p,0,0)
         time.sleep(0.000001)
         m = m+1
         v.after(1,Runner)

    
             

            

    

    
canvas = tkinter.Canvas(v,width=1800,height=700,bg="black")
runner=tkinter.PhotoImage(file="BlueCar.png")
p = canvas.create_image(50,50,image=runner)


Runner()
canvas.pack()

v.mainloop()

