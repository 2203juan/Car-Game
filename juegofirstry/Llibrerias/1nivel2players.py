import tkinter
import time
import random

# Crea la ventana que tendrá el mapa la asocia a la variable v
v = tkinter.Tk()
v.geometry("1890x1000")

#cargo las imágenes a usar
u=tkinter.PhotoImage(file="TryFont3.png")#carga imagen mapa
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







#widgest que se crearán a partit de las imágenes con canvas
mapajuego= fondojuego.create_image(850,300, image=u)#carga
x = fondojuego.create_image(100,600,image=carrov1)
k = fondojuego.create_image(97,50,image=vancar)
h=fondojuego.create_image(100,55, image=photo)
f=fondojuego.create_image(450, 55, image=fighter)


#funciones

def MiniVan():
    x=random.randint(0,50)
    global fondojuego, m
    
    fondojuego.move(k, 0, 5)
        

    m = m + 1
        
    if(fondojuego.coords(k)[1]>700):
        fondojuego.move(k,x,-700)

    if(fondojuego.coords(k)[0]>=310):
        fondojuego.move(k,-203,0)


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
   
    if(tecla == "'d'" or tecla=="'D'"):
        if(fondojuego.coords(x)[0] <300):
            
            i = i + 20
          
            fondojuego.move(x,15,0)
            
            
            """
        elif i ==430:
            fondojuego.delete(x)
            i = -100
            x = fondojuego.create_image(500+i,600+j,image=explosion)
            """
    if(tecla == "'a'" or tecla== "'A'"):
        if(fondojuego.coords(x)[0]> 110):
            
            i = i - 20
            fondojuego.move(x,-12,0)
            """
        else:
            fondojuego.delete(x)
            x = fondojuego.create_image(500+i,600+j,image=explosion)
            """




q= 0

def Runner():
    
    global fondojuego,h,q
    z =fondojuego.coords(h)[0]
    if((q>=0 and q<50)or (q>100 and q<150)):
       
        fondojuego.move(h,5,1)
        

    
        q = q+ 1
     

    elif(q<=100 or q<200):
         
         fondojuego.move(h,-5,5)
     
         q= q+1
    if(fondojuego.coords(h)[1]>600):
        fondojuego.move(h,100-z,-600)
        q=0
        




#llamado de funciones
def principal():
    fighteer()
    Runner()
    MiniVan()
    v.after(5,principal)
#RunnerCar()

principal()


# Liga el evento key al canvas
fondojuego.bind("<Key>", key)

# Pone el foco en el canvas
fondojuego.focus_set()

#enpaquetado( mostrar lo hecho con canvas)
fondojuego.pack()



#ciclo para escuchar los eventos
v.mainloop()
