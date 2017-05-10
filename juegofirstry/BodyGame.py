import tkinter
import time
import random

# Crea la ventana que tendrá el mapa la asocia a la variable v
ventana = tkinter.Tk()
ventana.title("Road Fighter")
ventana.geometry("1890x1000")
v = tkinter.Toplevel()
v.geometry("1890x1000")
imagen1 = tkinter.PhotoImage(file="fondoprincipal.png")
fondo = tkinter.Label(ventana, image=imagen1).place(x=0 ,y=0)
#cargo las imágenes a usar
u=tkinter.PhotoImage(file="TryFont3m.png")#carga imagen mapa
#photopo=tkinter.PhotoImage(file="Tryfont3m.png")
carrov1 = tkinter.PhotoImage(file="UserCare.png")#carro verde
carrov2 = tkinter. PhotoImage(file="UserCare.png")#carro verde
explosion = tkinter. PhotoImage(file="explosion1.png")#explosion de choque
photo=tkinter.PhotoImage(file="BlueCare.png")#CarroRunnerAzul
vancar=tkinter.PhotoImage(file="RedCare.png")#Carro Minivan rojo
fighter=tkinter.PhotoImage(file="YellowCare.png")
#cargo las imagenes de los botones
imagen_2boton=tkinter.PhotoImage(file="Level1.png")
imagen_3boton=tkinter.PhotoImage(file="Level2.png")
imagen_4boton=tkinter.PhotoImage(file="Level3.png")
imagen_5boton=tkinter.PhotoImage(file="Level4.png")
imagen_6boton=tkinter.PhotoImage(file="Level5.png")
imagen_1boton = tkinter.PhotoImage(file="BotonSalir.png")

#movimientofondo
#photopo=tkinter.PhotoImage(file="Tryfont3m.png")

#Doy título a mi Juego

Imagen = tkinter.Label(ventana,text="Road Fighter", font=("Tempus Sans ITC",72)).place(x=450, y=20)

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
mapajuego= fondojuego.create_image(680,200, image=u)#carga
x = fondojuego.create_image(100,600,image=carrov1)
k = fondojuego.create_image(97,50,image=vancar)
h=fondojuego.create_image(100,55, image=photo)
f=fondojuego.create_image(250, 55, image=fighter)

#movimientofondo
#po=fondojuego.create_image(680,200, image=photopo)


#funciones

def MiniVan(s):
    x=random.randint(0,50)
    global fondojuego, m
    
    fondojuego.move(k, 0, s)
        

    #m = m + 1
        
    if(fondojuego.coords(k)[1]>700):
        fondojuego.move(k,x,-700)

    if(fondojuego.coords(k)[0]>=310):
        fondojuego.move(k,-203,0)


def fighteer(X,Y):
     
        if(fondojuego.coords(x)[0]<fondojuego.coords(f)[0]):
            fondojuego.move(f,-X,Y)
            
        if(fondojuego.coords(x)[0]>fondojuego.coords(f)[0]):
            fondojuego.move(f,X,Y)
            
        if(fondojuego.coords(x)[0]==fondojuego.coords(f)[0]):
            fondojuego.move(f,0,Y)
        if(fondojuego.coords(f)[1]>700):
            fondojuego.move(f,0,-700)

#usercar

def key(event):
    """
    """
    global x,i,j
    tecla = repr(event.char)
   
    if(tecla == "'d'" or tecla=="'D'"):
        if(fondojuego.coords(x)[0] <330):
            
            i = i + 20
          
            fondojuego.move(x,15,0)
            
            
            """
        elif i ==430:
            fondojuego.delete(x)
            i = -100
            x = fondojuego.create_image(500+i,600+j,image=explosion)
            """
    if(tecla == "'a'" or tecla== "'A'"):
        if(fondojuego.coords(x)[0]> 90):
            
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
    if((q>=0 and q<50)or (q>100 and q<150) or (q>200 and q<250)):
       
        fondojuego.move(h,5,3)
        

    
        q = q+ 1
     

    elif(q<=100 or q<200 or q<250):
         
         fondojuego.move(h,-5,3)
     
         q= q+1
    if(fondojuego.coords(h)[1]>600):
        fondojuego.move(h,100-z,-600)
        q=0


def colisiones():
    
    x1=fondojuego.coords(x)[0]
    x2=fondojuego.coords(f)[0]
    x3=fondojuego.coords(k)[0]
    x4=fondojuego.coords(h)[0]
    y1=fondojuego.coords(x)[1]
    y2=fondojuego.coords(f)[1]
    y3=fondojuego.coords(k)[1]
    y4=fondojuego.coords(h)[1]

    #bordes
    if(x1<=90):
        coli=fondojuego.create_image(x1,y1,image=explosion)
        return True
    if(x1>=335):
        coli=fondojuego.create_image(x1,y1,image=explosion)
        return True
        
    
    """
    
    if(x1>=x2 and x1<=x2+40 and y1>=y2 and y1<=y2+81):
           coli=fondojuego.create_image(x1,y1,image=explosion)
           return True
    if(x1+40>=x2 and x1<=x2+40 and y1+40>=y2 and y1<=y2+81):
           coli=fondojuego.create_image(x1,y1,image=explosion)
           return True

    """
    


def fondomoving():
    #x=random.randint(0,50)
    global fondojuego, m,v
    
    
    fondojuego.move(mapajuego, 0, 15)
        

    m = m + 1
        
    #if(fondojuego.coords(po)[1]<6000):
        #fondojuego.move(po,0,1000)

    if(fondojuego.coords(mapajuego)[1]>3300):
        fondojuego.move(mapajuego,0,-fondojuego.coords(mapajuego)[1])

    v.after(10,fondomoving)
  
           


    
    

    
    
  

v1=0
v2=0
v3=0
F=0

#llamado de funciones
def principal():
    fighteer(F,v2)
    if(colisiones()):
        return 0
    Runner()
    MiniVan(v1)
    v.after(15,principal)
#RunnerCar()
def lvl1():
    global v1,v2,F,po
    fondojuego.focus_set()
    #v.after(5,fondomoving)
    v.deiconify()
    ventana.iconify()
    v1=2
    v2=3
    F=1
    fondomoving()
    principal()
    #colisiones()
v.iconify()
boton2=tkinter.Button(ventana, image=imagen_2boton,command=lvl1).place(x=1200, y=300)

def lvl2():
    global v1,v2,F
    fondojuego.focus_set()
    v.deiconify()
    ventana.iconify()
    v1=3
    v2=4
    F=1.5
    principal()
v.iconify()
boton3=tkinter.Button(ventana, image=imagen_3boton,command=lvl2).place(x=1200, y=350)

def lvl3():
    global v1,v2,F
    fondojuego.focus_set()
    v.deiconify()
    ventana.iconify()
    v1=5
    v2=7
    F=2
    principal()
v.iconify()
boton4=tkinter.Button(ventana, image=imagen_4boton,command=lvl3).place(x=1200, y=400)

def lvl4():
 global v1,v2,F
 fondojuego.focus_set()
 v.deiconify()
 ventana.iconify()
 v1=6
 v2=8
 F=5
 principal()
v.iconify()
boton5=tkinter.Button(ventana, image=imagen_5boton,command=lvl4).place(x=1200, y=450)

def lvl5():
 global v1,v2,F
 fondojuego.focus_set()
 v.deiconify()
 ventana.iconify()
 v1=10
 v2=10
 F=5
 principal()
v.iconify()
boton6=tkinter.Button(ventana, image=imagen_6boton,command=lvl5).place(x=1200, y=500)

boton1 = tkinter.Button(ventana, image=imagen_1boton,command=ventana.destroy).place(x=1200, y=600)
    


# Liga el evento key al canvas
fondojuego.bind("<Key>", key)

# Pone el foco en el canvas


#enpaquetado( mostrar lo hecho con canvas)
fondojuego.pack()



#ciclo para escuchar los eventos
v.mainloop()
