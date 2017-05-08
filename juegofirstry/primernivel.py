import tkinter
import time
import random

#cargo las imágenes a usar
u=tkinter.PhotoImage(file="TryFont1.png")#carga imagen mapa
carrov1 = tkinter.PhotoImage(file="UserCar.png")#carro verde
carrov2 = tkinter. PhotoImage(file="UserCar.png")#carro verde
explosion = tkinter. PhotoImage(file="explosion.png")#explosion de choque
photo=tkinter.PhotoImage(file="BlueCar.png")#CarroRunnerAzul
vancar=tkinter.PhotoImage(file="RedCar.png")#Carro Minivan rojo
fighter=tkinter.PhotoImage(file="YellowCar.png")

#defino las variables abiertas (no definidas dentro de las funciones)que voy a usar dentro de mis funciones
presiono = False
x = None
i = 0
j = 0
m= 0
i=0
z=0

g = 0
c = 0
d = 5





#defino canvas principal
fondojuego=tkinter.Canvas(v, width=1350, height=700,bd=0,highlightthickness=0)





"""

#widgest que se crearán a partit de las imágenes con canvas
mapajuego= fondojuego.create_image(850,300, image=u)#carga
x = fondojuego.create_image(500,600,image=carrov1)
k = fondojuego.create_image(500,50,image=vancar)
h=fondojuego.create_image(400,55, image=photo)
f=fondojuego.create_image(450, 55, image=fighter)
"""

def MiniVan():
    global fondojuego, m
    
    fondojuego.move(k, 0, 5)
        

    m = m + 1
        
    if(fondojuego.coords(k)[1]>700):
        fondojuego.move(k,0,-700)

def fighteer():
     
        if(fondojuego.coords(x)[0]<fondojuego.coords(f)[0]):
            fondojuego.move(f,-1,1)
            
        elif(fondojuego.coords(x)[0]>fondojuego.coords(f)[0]):
            fondojuego.move(f,1,1)
            
        if(fondojuego.coords(x)[0]==fondojuego.coords(f)[0]):
            fondojuego.move(f,0,1)
        if(fondojuego.coords(f)[1]>700):
            fondojuego.move(f,0,-700)

#usercar

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



            """

ma=0
za=0




"""
            """
            def RunnerCar():
    global  ma,za,fondojuego,v
    while ma>=0 and ma <=160:
                i=0
                for ma in range(40,100):
                    fondojuego.move(h,6,z)
                    v.update()
                    time.sleep(0.01)
                    ma=ma+0.01
                    za=za+0.001

                for ma in range(40,100):
                    fondojuego.move(h,-6,z)
                    v.update()
                    time.sleep(0.01)
                    ma=ma
                    za=za+0.001"""
                    

"""

"""
q= 0


def Runner():
  
    global fondojuego,h,q
    if((q>=0 and q<50)or (q>100 and q<150)):
       
        fondojuego.move(h,10,1)
        
        

    
        q = q+ 1
     

    elif(q<=100 or q<200):
         
         fondojuego.move(h,-10,5)
     
         q= q+1
    if(fondojuego.coords(h)[1]>600):
        fondojuego.move(h,0,-600)
        q=0
        



"""
             




  

#RunnerCar

def RunnerCar():
    global c,g,d



    while g >= 0 and c <= 4:
        g = 0
        for i in range(0, 120 - d):
            fondojuego.move(h, 5, c)
            #v.after(0,RunnerCar)
            time.sleep(0.01)
            g = g + 0.01
            c = c + 0.01
            v.after(1, RunnerCar)

        for g in range(0, 135):
            fondojuego.move(h, -4, c)
            #v.after(0, RunnerCar)
            time.sleep(0.01)
            g = g + 1
            c = c + 0.01
            v.after(1, RunnerCar)

"""
#llamado de funciones
def principal():
    fighteer()
    Runner()
    MiniVan()
    v.after(5,principal)
#RunnerCar()

def nivel1():

    # Crea la ventana que tendrá el mapa la asocia a la variable v
    v = tkinter.Tk()
    v.geometry("1890x1000")

    #cargo las imágenes a usar
    u=tkinter.PhotoImage(file="TryFont1.png")#carga imagen mapa
    carrov1 = tkinter.PhotoImage(file="UserCar.png")#carro verde
    carrov2 = tkinter. PhotoImage(file="UserCar.png")#carro verde
    explosion = tkinter. PhotoImage(file="explosion.png")#explosion de choque
    photo=tkinter.PhotoImage(file="BlueCar.png")#CarroRunnerAzul
    vancar=tkinter.PhotoImage(file="RedCar.png")#Carro Minivan rojo
    fighter=tkinter.PhotoImage(file="YellowCar.png")

    #defino las variables abiertas (no definidas dentro de las funciones)que voy a usar dentro de mis funciones
    presiono = False
    x = None
    i = 0
    j = 0
    m= 0
    i=0
    z=0

    g = 0
    c = 0
    d = 5

    posx1 = 100
    posy1 = 100
    posx2 = 500
    posy2 = 800





    #defino canvas principal
    fondojuego=tkinter.Canvas(v, width=1350, height=700,bd=0,highlightthickness=0)







    #widgest que se crearán a partit de las imágenes con canvas
    mapajuego= fondojuego.create_image(850,300, image=u)#carga
    x = fondojuego.create_image(500,600,image=carrov1)
    k = fondojuego.create_image(500,50,image=vancar)
    h=fondojuego.create_image(400,55, image=photo)
    f=fondojuego.create_image(450, 55, image=fighter)


    #funciones



    #principal()


    # Liga el evento key al canvas
    fondojuego.bind("<Key>", key)

    # Pone el foco en el canvas
    fondojuego.focus_set()

    #enpaquetado( mostrar lo hecho con canvas)
    fondojuego.pack()

    principal()



    #ciclo para escuchar los eventos
    v.mainloop()
nivel1()
