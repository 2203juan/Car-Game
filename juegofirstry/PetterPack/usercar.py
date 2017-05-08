import tkinter
import time

# Crea la ventana mapa la asocia a la variable v
v = tkinter.Tk()
v.geometry("1890x1000")

presiono = False
x = None
i = 0
j = 0


#defino el canvas a usar
fondojuego=tkinter.Canvas(v, width=1350, height=700,bd=0,highlightthickness=0)

m= 0
posx1 = 100
posy1 = 100
posx2 = 500
posy2 = 800

def movimiento():
    """
    """
    global v,canvas,p,m,posx1,posy1,posx2,posy2
    if(m<500):
        canvas.move(p,0,2)
    
        m = m+ 1
        posx1 = posx1 + 1
        posy1 = posy1 + 1
        posx2 = posx2 - 1
        posy2 = posy2 - 1

        if(posx1 <= posx2 and posx2 <= posx1 + 50 and posy1 <= posy2 and posy2 <= posy1 + 50):
            v.after(5,movimiento)
            
        else:
            v.after(10,movimiento)
        

canvas = tkinter.Canvas(v,width=500,height=500)
canvas.pack()
vancar=tkinter.PhotoImage(file="RedCar.png")
p = canvas.create_image(50,50,image=vancar)

movimiento()








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
    x = d.create_image(500+i,600+j,image=filename2)

def key(event):
    """
    """
    global x,i,j
    tecla = repr(event.char)
    print(tecla)
    if(tecla == "'d'" ):
        if(i < 440):
            fondojuego.delete(x)
            i = i + 10
            x = fondojuego.create_image(500+i,600+j,image=carrov1)
            """
        elif i ==430:
            fondojuego.delete(x)
            i = -100
            x = fondojuego.create_image(500+i,600+j,image=explosion)
            """
    if(tecla == "'a'"):
        if(i > -90):
            fondojuego.delete(x)
            i = i - 10
            x = fondojuego.create_image(500+i,600+j,image=carrov2)
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
x = fondojuego.create_image(500,600,image=carrov1)
u=tkinter.PhotoImage(file="TryFont.png")#carga imagen mapa

mapa= fondojuego.create_image(850,300, image=u)
"""
i=0
z=0



photo=tkinter.PhotoImage(file="BlueCar.png")
p=fondojuego.create_image(350,55, image=photo)

def RunnerCar():
    global  i,z
    while i>=0 and i <=900:
                i=0
                for i in range(750,850):
                    fondojuego.move(p,6,z)
                    v.update()
                    time.sleep(0.03)
                    i=i+0.01
                    z=z+0.01

                for i in range(765,850):
                    fondojuego.move(p,-6,z)
                    v.update()
                    time.sleep(0.03)
                    i=i
                    z=z+0.01
                    
                    
fondojuego.pack()
RunnerCar()



"""


# Ciclo para escuchar los eventos
v.mainloop()

