import tkinter
import time

v=tkinter.Tk()
v.geometry("1890x1000")
m=0

fondojuego=tkinter.Canvas(v, width=1350, height=700,bd=0,highlightthickness=0)




photopo=tkinter.PhotoImage(file="Tryfont3m.png")
po=fondojuego.create_image(680,200, image=photopo)

"""

def fondomoving():
  
    

    for i in range(0,450):
                    fondojuego1.move(po,0,5)
                    v.update()
                

        
    while(fondojuego1.coords(po)[1]>800):
        fondojuego1.move(po,0,-800)
        v.update()


    while fondojuego1.coords(po)[0]>=0:
        fondojuego1.move(po,0,5)
        v.update()
        fondomoving()
        


fondojuego1.focus_set()
v.after(5,fondomoving)

fondojuego1.pack()
"""

def fondomoving():
    #x=random.randint(0,50)
    global fondojuego, m,v
    
    
    fondojuego.move(po, 0, 15)
        

    m = m + 1
        
    #if(fondojuego.coords(po)[1]<6000):
        #fondojuego.move(po,0,1000)

    if(fondojuego.coords(po)[1]>3300):
        fondojuego.move(po,0,-fondojuego.coords(po)[1])

    v.after(10,fondomoving)
"""
def moving():
     global fondojuego, m
    
    fondojuego.move(k, 0, s)
        

    m = m + 1
        
    if(fondojuego.coords(k)[1]>700):
        fondojuego.move(k,x,-700)

    if(fondojuego.coords(k)[0]>=310):
        fondojuego.move(k,-203,0)
"""

fondojuego.pack()
MiniVan()


v.mainloop()
