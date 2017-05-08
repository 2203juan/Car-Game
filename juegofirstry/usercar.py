import tkinter
import time
import random

# Crea la ventana mapa la asocia a la variable v
v = tkinter.Tk()
v.geometry("1890x1000")

presiono = False
x = None
i = 0
j = 0


#defino el canvas a usar
fondojuego=tkinter.Canvas(v, width=1350, height=700,bd=0,highlightthickness=0)








def derecha():
    """
    """
    global presiono,x,i,j
    fondojuego.delete(x)
    i = i + 10
    x = d.create_image(500+i,600+j,image=carrov1)

def izquierda():
    """
    """
    global presiono,x,i,j
    fondojuego.delete(x)
    i = i - 10
    x = d.create_image(500+i,600+j,image=carrov1)

def key(event):
    """
    """
    global x,i,j
    tecla = repr(event.char)
    #print(tecla)
    if(tecla == "'d'" ):
        if(i < 440):
            #fondojuego.delete(x)
            i = i + 20
           # x = fondojuego.create_image(500+i,600+j,image=carrov1)
            fondojuego.move(x,20,0)
            """
        elif i ==430:
            fondojuego.delete(x)
            i = -100
            x = fondojuego.create_image(500+i,600+j,image=explosion)
            """
    if(tecla == "'a'"):
        if(i > -90):
            #fondojuego.delete(x)
            i = i - 20
            fondojuego.move(x,-20,0)
            """
        else:
            fondojuego.delete(x)
            x = fondojuego.create_image(500+i,600+j,image=explosion)
            """

# Crea  el canvas 




# Liga el evento key al canvas
fondojuego.bind("<Key>", key)

# Pone el foco en el canvas
fondojuego.focus_set()


# Empaqueta (muestra) los widgets

fondojuego.pack()




# Carga una imagen
carrov1 = tkinter.PhotoImage(file="UserCar.png")
carrov2 = tkinter. PhotoImage(file="UserCar.png")
explosion = tkinter. PhotoImage(file="explosion.png")
s= fondojuego.create_image(500,600,image=carrov1)
u=tkinter.PhotoImage(file="TryFont1.png")#carga imagen mapa
vancar=tkinter.PhotoImage(file="RedCar.png")


mapa= fondojuego.create_image(850,300, image=u)
x = fondojuego.create_image(500+i,600+j,image=carrov1)


p = fondojuego.create_image(420,50,image=vancar)


photo=tkinter.PhotoImage(file="BlueCar.png")
bluexxx=fondojuego.create_image(620,55, image=photo)


m= 0


def MiniVan():
 
    global fondojuego,m
    
    fondojuego.move(p,0,2)
    
    m = m+ 1
    v.after(10,MiniVan)

"""
def RunnerCar():
    g=0
    c=0
    d=5
    
    
    while g>=0 and c <=4:
                g=0
                for i in range(0,120-d):
                    fondojuego.move(p,5,c)
                    v.update()
                    time.sleep(0.01)
                    g=g+0.01
                    c=c+0.01

                for g in range(0,135):
                    fondojuego.move(p,-4,c)
                    v.update()
                    time.sleep(0.01)
                    g=g+1
                    c=c+0.01


"""


 
                    
                    


#RunnerCar()
MiniVan()



             





fondojuego.pack()
# Ciclo para escuchar los eventos
v.mainloop()

