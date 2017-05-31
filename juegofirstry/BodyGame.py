#----------------------------------------------------ROAD FIGHTER-----------------------------------------------------------#
#----------------------------------ELABORADO POR JUA JOSÉ HOYOS URCUE---------------------------------#
#----------------------------------PONTIFICIA UNIVERSIDAD JAVERIANA CALI---------------------------------#
#----------------------------------INGENIERÍA DE SISTEMAS Y COMPUTACIÓN---------------------------------#
#---------------------------------------------------------2017-1---------------------------------------------------------------------#



import tkinter
import time
import random
import math
import pygame
from pygame.locals import * #solo para la música

pygame.mixer.init()


musicaMenu = pygame.mixer.Sound("menu.wav")
sonidoacelerar=pygame.mixer.Sound("acelerate.wav")
sonidofail=pygame.mixer.Sound("loser.wav")
crash=pygame.mixer.Sound("choque.wav")

recarga=pygame.mixer.Sound("gasolina.wav")









musicaMenu.play()

# Crea la ventana que tendrá el menú asociado a la variable ventana
ventana = tkinter.Tk()
ventana.title("Road Fighter")
ventana.geometry("1500x900")
v = tkinter.Toplevel()
v.geometry("1500x900")
imagen1 = tkinter.PhotoImage(file="fondoprincipal.png")
fondomenu = tkinter.Label(ventana, image=imagen1).place(x=0 ,y=0)





#Boton de instrucciones del juego

instructions=tkinter.Button(ventana,text="¿Cómo jugar?").place(x=20, y= 500 )



#x=tkinter.StringVar()
fondojuego =tkinter.Canvas(v,height=600,width=900,bg="black")

ho= []

var=tkinter.StringVar()#charge textvariable
#fondotextos= tkinter.Label(ventana,textvariable =var,bg="black",fg="white")
#cargo las imágenes a usar


#fondos primer nivel
fondomarder=tkinter.PhotoImage(file="marderecha.png")
fondomarizq=tkinter.PhotoImage(file="marizq.png")
centro1=tkinter.PhotoImage(file="centermar.png")


#fondos segundo nivel
fondotierraizq=tkinter.PhotoImage(file="tierraizq.png")
fondotierrader=tkinter.PhotoImage(file="tierrader.png")
centro2=tkinter.PhotoImage(file="centertierra.png")

#fondos tercer nivel

moradoizq=tkinter.PhotoImage(file="fondo3izq.png")
moradoder=tkinter.PhotoImage(file="fondo3der.png")
centro3=tkinter.PhotoImage(file="centermora.png")

#fondos cuarto nivel

rojoizq=tkinter.PhotoImage(file="rojoizq.png")
rojoder=tkinter.PhotoImage(file="rojoder.png")
centro4=tkinter.PhotoImage(file="centerrojo.png")

#fondos quinto nivel

spaceizq=tkinter.PhotoImage(file="spaceizq.png")
spaceder=tkinter.PhotoImage(file="spaceder.png")
centro5=tkinter.PhotoImage(file="spacecenter.png")



#Entradas para ingresar y mostrar los nombres de los jugadores
#1
nombre=tkinter.StringVar ()
nombre.set("")
instruccion_nombre1= tkinter.Label(ventana,text="Nombre del jugador 1", font=("Tempus Sans ITC",12),fg="black").place(x=20, y=395)
nombrecaja = tkinter.Entry(ventana,font=("Tempus Sans ITC",12), textvariable=nombre).place(x=180, y = 395)
muestraplayer1= tkinter.Label(v,textvariable=nombre, font=("Tempus Sans ITC",12),fg="black")

#2
nombre2=tkinter.StringVar()
nombre2.set("")
instruccion_nombre2= tkinter.Label(ventana,text="Nombre del jugador 2", font=("Tempus Sans ITC",12)).place(x=20, y=445)
nombrecaja2 = tkinter.Entry(ventana,font=("Tempus Sans ITC",12) ,textvariable=nombre2).place(x=180, y = 445)
muestraplayer2= tkinter.Label(v,textvariable=nombre2, font=("Tempus Sans ITC",12),fg="black")






#photopo=tkinter.PhotoImage(file="Tryfont3m.png")
carrov1 = tkinter.PhotoImage(file="UserCare.png")#carro verde
carrov2 = tkinter. PhotoImage(file="UserCare.png")#carro verde
explosion = tkinter. PhotoImage(file="explosion1.png")#explosion de choque
photo=tkinter.PhotoImage(file="BlueCare.png")#CarroRunnerAzul
vancar=tkinter.PhotoImage(file="RedCare.png")#Carro Minivan rojo
fighter=tkinter.PhotoImage(file="YellowCare.png")
usuariouno45= tkinter.PhotoImage(file="jugador145.png")

user2=tkinter.PhotoImage(file="usercar2e.png")



minivan2=tkinter.PhotoImage(file="RedCare.png")

run2=tkinter.PhotoImage(file="BlueCare.png")


fi2=tkinter.PhotoImage(file="YellowCare.png")

chargegas=tkinter.PhotoImage(file="Recarga.png")
chargegas2=tkinter.PhotoImage(file="Recarga.png")

mancha1=tkinter.PhotoImage(file="aceite.png")
mancha2=tkinter.PhotoImage(file="aceite.png")

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
q=0
g = 0       
c = 0
d = 5







        





#defino canvas principal
fondojuego=tkinter.Canvas(v, width=1350, height=700,bd=0,highlightthickness=0)





#widgest que se crearán a partit de las imágenes con canvas
#mapajuego= fondojuego.create_image(680,200, image=u)#carga





#widgest del fondo nivel1
mard=fondojuego.create_image(1145,55, image=fondomarder)
mari=fondojuego.create_image(230,55, image=fondomarizq)
c1=fondojuego.create_image(695,380, image=centro1)#centro estático


# widgest del fondo nivel 2
tierrizq=fondojuego.create_image(230,55, image=fondotierraizq)
tierrder=fondojuego.create_image(1145,55,image=fondotierrader)
c2=fondojuego.create_image(690,380, image=centro2)#centro estático

#widgest del fondo nivel 3

moraizq=fondojuego.create_image(230,55, image=moradoizq)
morader=fondojuego.create_image(1145,55, image=moradoder)
c3=fondojuego.create_image(690,380,image=centro3)

#widgest del fondo nivel 4

roizq=fondojuego.create_image(230,55, image=rojoizq)
roder=fondojuego.create_image(1140,55, image=rojoder)
c4=fondojuego.create_image(690, 380, image= centro4)

#widgest del fondo nivel 5

sizq=fondojuego.create_image(230,55, image= spaceizq)
sder=fondojuego.create_image(1145,55, image=spaceizq)
c5=fondojuego.create_image(690,380,image=centro5)






#widgest de carros, obastáculos y enemigos jugador 1
x = fondojuego.create_image(100,600,image=carrov1)
k = fondojuego.create_image(97,50,image=vancar)
h=fondojuego.create_image(150,55, image=photo)
f=fondojuego.create_image(250, 55, image=fighter)
#widgest de carros, obastáculos y enemigos jugador 2
van2=fondojuego.create_image(1220,50,image=minivan2)
u2=fondojuego.create_image(1250,600, image= user2)
f2=fondojuego.create_image(1250, 55, image=fi2)
r2=fondojuego.create_image(1100,55, image=run2)
ga=fondojuego.create_image(200,55, image=chargegas)
ga2=fondojuego.create_image(1300,55, image=chargegas2)
ma1=fondojuego.create_image(120,50,image=mancha1)
ma2=fondojuego.create_image(1220,50,image=mancha1)




#movimientofondo
#po=fondojuego.create_image(680,200, image=photopo)


#defino las funciones que van a dinamizar mi juego










def MiniVan(s):
    """
    Esta función mueve verticalmente la MiniVan, un carro de color rojo, cuyo objetivo es moverse verticalmente hacia abajo, siendo un   obstáculo
    para el jugador, que por cierto es el menos peligroso, ya que no cambia de carril mientras se mueve, es decir, su movimiente es constante.
    
    """
    x=random.randint(0,50)
    global fondojuego, m
    
    fondojuego.move(k, 0, s)
        
    if(fondojuego.coords(k)[1]>700):
        fondojuego.move(k,x,-700)

    if(fondojuego.coords(k)[0]>=310):
        fondojuego.move(k,-203,0)

def MiniVan2(s):
    """
    Esta función mueve verticalmenta la MiniVan, un carro de color rojo, cuyo objetivo es moverse verticalmente hacia abajo, siendo un   obstáculo
    para el jugador, que por cierto es el menos peligroso, ya que no cambia de carril mientras se mueve, es decir, su movimiente es constante.
    
    """
    global fondojuego, m

    x=random.randint(0,50)
  
    
    fondojuego.move(van2, 0, s)
        
    if(fondojuego.coords(van2)[1]>700):
        fondojuego.move(van2,x,-700)

    if(fondojuego.coords(van2)[0]>=1220):
        fondojuego.move(van2,-203,0)


def mancha(s):
    
    """
    Esta función mueve verticalmente la mancha de aceite, de color negro, cuyo objetivo es moverse verticalmente hacia abajo, siendo un   obstáculo
    para el jugador, en el cual se puede resbalar, aunque el código que lo hace resbalar se encuentra en las colisiones
    
    """
    global fondojuego
    x=random.randint(0,50)
    mm=random.randint(-5000,-3000)
    
    fondojuego.move(ma1, 0, s)
        
    if(fondojuego.coords(ma1)[1]>700):
        fondojuego.move(ma1,x,mm)

    if(fondojuego.coords(ma1)[0]>=310):
        fondojuego.move(ma1,-203,0)

def mancha2(s):
    """
    Esta función mueve verticalmente la mancha de aceite, de color negro, cuyo objetivo es moverse verticalmente hacia abajo, siendo un   obstáculo
    para el jugador, en el cual se puede resbalar, aunque el código que lo hace resbalar se encuentra en las colisiones
    
    """
    global fondojuego, m
    mm=random.randint(-5000,-3000)
    x=random.randint(0,100)
  
    
    fondojuego.move(ma2, 0, s)
        
    if(fondojuego.coords(ma2)[1]>700):
        fondojuego.move(ma2,x,mm)

    if(fondojuego.coords(ma2)[0]>=1220):
        fondojuego.move(ma2,-203,0)

        
def Fighter2(X,Y):
        """
        Esta función mueve al carro de color amarillo , cuyo objetivo es perseguir al carro del jugador para chocarlo, es el enemigo más peligroso de los tres,
        ya que ataca directamente al carro del jugador.
        
        """
     
        if(fondojuego.coords(u2)[0]<fondojuego.coords(f2)[0]):
            fondojuego.move(f2,-X,Y)
            
        if(fondojuego.coords(u2)[0]>fondojuego.coords(f2)[0]):
            fondojuego.move(f2,X,Y)
            
        if(fondojuego.coords(u2)[0]==fondojuego.coords(f2)[0]):
            fondojuego.move(f2,0,Y)
        if(fondojuego.coords(f2)[1]>700):
            fondojuego.move(f2,0,-700)


def Fighter(X,Y):
        """
        Esta función mueve al carro de color amarillo , cuyo objetivo es perseguir al carro del jugador para chocarlo, es el enemigo más peligroso de los tres,
        ya que ataca directamente al carro del jugador.
        
        """
     
        if(fondojuego.coords(x)[0]<fondojuego.coords(f)[0]):
            fondojuego.move(f,-X,Y)
            
        if(fondojuego.coords(x)[0]>fondojuego.coords(f)[0]):
            fondojuego.move(f,X,Y)
            
        if(fondojuego.coords(x)[0]==fondojuego.coords(f)[0]):
            fondojuego.move(f,0,Y)
        if(fondojuego.coords(f)[1]>700):
            fondojuego.move(f,0,-700)

def charge(s):
    """
    Esta función mueve verticalmenta la nave de recarga, la cuál permitirá que el usuario que pase por encima de ella recargue un poco su combustible
    aunque el código que hace que se recargue la gasolina se encuentra en la función de las colisiones.
    
    """
    global fondojuego, m

    x=random.randint(0,50)
  
    
    fondojuego.move(ga, 0, s)
        
    if(fondojuego.coords(ga)[1]>700):
        fondojuego.move(ga,x,-3000)

    if(fondojuego.coords(ga)[0]>=300):
        fondojuego.move(ga,-203,0)

def charge2(s):
    """
    Esta función mueve verticalmenta la nave de recarga, la cuál permitirá que el usuario que pase por encima de ella recargue un poco su combustible
    aunque el código que hace que se recargue la gasolina se encuentra en la función de las colisiones.
    
    """
    global fondojuego, m

    x=random.randint(0,50)
  
    
    fondojuego.move(ga2, 0, s)
        
    if(fondojuego.coords(ga2)[1]>700):
        fondojuego.move(ga2,x,-700)

    if(fondojuego.coords(ga2)[0]>=1220):
        fondojuego.move(ga2,-203,0)


#usercar

def keyup(e):
  global x,ho

  if(e.keycode in ho):
    ho.pop(ho.index(e.keycode))
   

def keydown(e):
  global x,ho
  if not e.keycode in ho:
      
    ho.append(e.keycode)
  
     
def key():
  global ho
  if(65 in ho):  #letra A en código ascii
    fondojuego.move(x,-5,0)
 
  if(68 in ho):
    fondojuego.move(x,5,0) #letra D en código ascii
  
def key2():
    
    if(37 in ho):
        fondojuego.move(u2,-5,0) #flecha de dirección izquiera en código ascii
    if(39 in ho):
        fondojuego.move(u2,5,0) #flecha de dirección derecha en código ascii

    



def Runner():
    """
    Esta función se encarga de mover el carro azul, cuyo objetivo es tratar de chocar al carro del jugador,cambiando de carril constantemente
    mientras se mueve verticalmente hacia abajo y horizontalmente de derecha a izquierda y visceversa.

    """
    vv=3
    z =fondojuego.coords(h)[0]
    b= 7
    
    y= math.sin(2*fondojuego.coords(h)[1]*math.pi/(300))*b
    if(fondojuego.coords(h)[1]>600):
        fondojuego.move(h,100-z,-600)
        q=0
    fondojuego.move(h,y,vv)


def Runner2():
    """
    Esta función se encarga de mover el carro azul, cuyo objetivo es tratar de chocar al carro del jugador,ncambiando de carril constantemente
    mientras se mueve verticalmente hacia abajo y horizontalmente de derecha a izquierda y visceversa.

    """
    vv=3
    z =fondojuego.coords(r2)[0]
    b= 7
    
    y= math.sin(2*fondojuego.coords(r2)[1]*math.pi/(300))*b
    if(fondojuego.coords(r2)[1]>=600):
        fondojuego.move(r2,1015-z,-600)
        q=0
    fondojuego.move(r2,y,vv)
def colisionesbor():
    """
    Esta función se encarga de hacer el efecto de explosión cuando el carro del jugador uno toca alguno de los dos extremos de la carretera, implicando
    que si esto sucede, el jugador habrá perdido la partida. 
    
    """
    
    x1=fondojuego.coords(x)[0]
    y1=fondojuego.coords(x)[1]
   

    if(x1<=85):
        coli=fondojuego.create_image(x1,y1,image=explosion)
        return True
    if(x1>=350):
        coli=fondojuego.create_image(x1,y1,image=explosion)
        return True


def colisionesbor2():
    """
    Esta función se encarga de hacer el efecto de explosión cuando el carro del jugador dos  toca alguno de los dos extremos de la carretera, implicando
    que si esto sucede, el jugador habrá perdido la partida.
    
    """
    
  
    x2= fondojuego.coords(u2)[0]
    y2=fondojuego.coords(u2)[1]
   

   
    if(x2<=1005):
        coli=fondojuego.create_image(x2,y2,image=explosion)
        return True
    if(x2>=1275):
        coli=fondojuego.create_image(x2,y2,image=explosion)
        return True

def destruirall():

    v.destroy()
    ventana.destroy()




    

        
    
  

ii=0

def colisionescarros():
    global x,contadorg1, contadorv1
    '''
    Esta función se encarga de hacer el efecto de choque entre el carro del jugador uno y los enemigos, además permite recargar de gasolina con la
    nave de recarga, y a su vez resbalar en la mancha de aceite.

    '''
  



    x1=fondojuego.coords(x)[0]
    x2=fondojuego.coords(f)[0]
    x3=fondojuego.coords(k)[0]
    x4=fondojuego.coords(h)[0]
    y1=fondojuego.coords(x)[1]
    y2=fondojuego.coords(f)[1]
    y3=fondojuego.coords(k)[1]
    y4=fondojuego.coords(h)[1]
    xr=fondojuego.coords(ga)[0]
    yr=fondojuego.coords(ga)[1]
    xm=fondojuego.coords(ma1)[0]
    ym=fondojuego.coords(ma1)[1]
    mm=random.randint(-7000,-5000)
    

    #con el fighter
   
    if(x1>=x2 and x1<=x2+26 and y1>=y2 and y1<=y2+53):
           #nivel1sound.stop()
           crash.play()
           sonidofail.play()

           coli=fondojuego.create_image(x1,y1,image=explosion)
           boton1 = tkinter.Button(v, text="Salir: si aun tienes las hagllas para jugar, ábreme de nuevo",command=destruirall).place(x=550, y=655)
           contadorg1=0
           contadorv1= contadorv1-5
        
           


    elif(x1+26>=x2 and x1<=x2+26 and y1+26>=y2 and y1<=y2+53):
              #nivel1sound.stop()
              crash.play()
              sonidofail.play()
              coli=fondojuego.create_image(x1,y1,image=explosion)
              boton1 = tkinter.Button(v, text="Salir: si aun tienes las hagllas para jugar, ábreme de nuevo",command=destruirall).place(x=550, y=655)
              contadorg1=0
              contadorv1= contadorv1-5
              

    #con la van

   
    if(x1>=x3 and x1<=x3+26 and y1>=y3 and y1<=y3+53):
        crash.play()
        fondojuego.move(x,5,0)
        contadorg1=contadorg1-250
        contadorv1= contadorv1-5
        if (fondojuego.move(x,5,0)):
            fondojuego.move(x, 0,-5)


    elif(x1+26>=x3 and x1<=x3+26 and y1+26>=y3 and y1<=y3+53):
            crash.play()
            if (fondojuego.move(x,-5,0)):
                fondojuego.move(x, 0,-5)

    # con el runner

       
    if(x1>=x4 and x1<=x4+26 and y1>=y4 and y1<=y4+52):
        crash.play()
        fondojuego.move(x,5,0)
        contadorg1=contadorg1-250
        contadorv1= contadorv1-5
        if (fondojuego.move(x,5,0)):
            fondojuego.move(x, 0,-5)


    elif(x1+26>=x4 and x1<=x4+26 and y1+26>=y4 and y1<=y4+52):
            crash.play()
            if (fondojuego.move(x,-5,0)):
                fondojuego.move(x, 0,-5)


    #recargador de gasolina

    

    if(x1>=xr and x1<=xr+30 and y1>=yr and y1<=yr+35):
         fondojuego.move(ga,0, mm)
         recarga.play()
         contadorg1=contadorg1+1000

        

    elif(x1+26>=xr and x1<=xr+30 and y1+26>=yr and y1<=yr+35):

         fondojuego.move(ga,0, mm)
         recarga.play()
         contadorg1=contadorg1+1000

    #mancha de aceite

    if(x1>=xm and x1<=xm+40 and y1>=ym and y1<=ym+40):
         fondojuego.move(x,7, 0)
         contadorg1=contadorg1-200
         contadorv1= contadorv1-5
         

    elif(x1+26>=xm and x1<=xm+40 and y1+26>=ym and y1<=ym+40):

         fondojuego.move(x,7, 0)
         contadorg1=contadorg1-200
         contadorv1= contadorv1-5
         


def colisionescarros2():
    global x,contadorg2, contadorv2
    '''
    Esta función se encarga de hacer el efecto de choque entre el carro del jugador dos y los enemigos, además permite recargar de gasolina con la
    nave de recarga, y a su vez resbalar en la mancha de aceite.

    '''
  
  
    

    x1=fondojuego.coords(u2)[0]
    x2=fondojuego.coords(f2)[0]
    x3=fondojuego.coords(van2)[0]
    x4=fondojuego.coords(r2)[0]
    y1=fondojuego.coords(u2)[1]
    y2=fondojuego.coords(f2)[1]
    y3=fondojuego.coords(van2)[1]
    y4=fondojuego.coords(r2)[1]
    xr=fondojuego.coords(ga2)[0]
    yr=fondojuego.coords(ga2)[1]
    xm=fondojuego.coords(ma2)[0]
    ym=fondojuego.coords(ma2)[1]
    mm=random.randint(-7000,-5000)
    

    # con el fighter
   
    if(x1>=x2 and x1<=x2+26 and y1>=y2 and y1<=y2+52):

           crash.play()
           sonidofail.play()
           coli=fondojuego.create_image(x1,y1,image=explosion)
           boton1 = tkinter.Button(v, text="Salir: si aun tienes las hagllas para jugar, ábreme de nuevo",command=destruirall).place(x=550, y=655)
           contadorg2=0
           contadorv2= contadorv2-5

    elif(x1+26>=x2 and x1<=x2+26 and y1+26>=y2 and y1<=y2+52):

           crash.play()
           sonidofail.play()
           coli=fondojuego.create_image(x1,y1,image=explosion)
           boton1 = tkinter.Button(v, text="Salir: si aun tienes las hagllas para jugar, ábreme de nuevo",command=destruirall).place(x=550, y=655)
           contadorg2=0
           contadorv2= contadorv2-5
                
    #con la van


    if(x1>=x3 and x1<=x3+26 and y1>=y3 and y1<=y3+53):
        crash.play()
        fondojuego.move(u2,5,0)
        contadorg2=contadorg2-250
        contadorv2= contadorv2-5   
        if (fondojuego.move(u2,5,0)):
            fondojuego.move(u2, 0,-5)

    elif(x1+26>=x3 and x1<=x3+26 and y1+26>=y3 and y1<=y3+53):
            crash.play()
            if (fondojuego.move(u2,-5,0)):
                fondojuego.move(u2, 0,-5)

    # con el runner

    if(x1>=x4 and x1<=x4+26 and y1>=y4 and y1<=y4+53):
        crash.play()
        fondojuego.move(u2,5,0)
        contadorg2=contadorg2-250
        contadorv2= contadorv2-5
        if (fondojuego.move(u2,5,0)):
            fondojuego.move(u2, 0,-5)

    elif(x1+26>=x4 and x1<=x4+26 and y1+26>=y4 and y1<=y4+53):
            crash.play()
            if (fondojuego.move(u2,-5,0)):
                fondojuego.move(u2, 0,-5)


    #recargador de gasolina


    if(x1>=xr and x1<=xr+30 and y1>=yr and y1<=yr+35):
         fondojuego.move(ga2,0, mm)
         recarga.play()
         contadorg2=contadorg2+1000

    elif(x1+26>=xr and x1<=xr+30 and y1+26>=yr and y1<=yr+35):
         fondojuego.move(ga2,0, mm)
         recarga.play()
         contadorg2=contadorg2+1000
    #mancha de aceite

    if(x1>=xm and x1<=xm+40 and y1>=ym and y1<=ym+40):
         fondojuego.move(u2,7, 0)
         contadorg2=contadorg2-200
         contadorv2= contadorv2-5
         

    elif(x1+26>=xm and x1<=xm+40 and y1+26>=ym and y1<=ym+40):

         fondojuego.move(u2,7, 0)
         contadorg2=contadorg2-200
         contadorv2= contadorv2-5




    

              

          
           


    

velocidadfondo=15
def fondomoving(fondoizquierda,velocidad):

    """
    Esta función se encarga de mover la parte izquierda de los fondos, con el fin de crear el efecto de aceleración

    """

    global fondojuego, v, velocidadfondo
    

    fondojuego.move(fondoizquierda, 0, velocidadfondo)
    if(fondojuego.coords(fondoizquierda)[1]>2500):
            fondojuego.move(fondoizquierda,0,-fondojuego.coords(fondoizquierda)[1])

def fondomoving2(fondoderecha,velocidad):
    """
    Esta función se encarga de mover la parte derecha de los fondos, con el fin de crear el efecto de aceleración

    """

    global fondojuego, v, velocidadfondo
    

        
    fondojuego.move(fondoderecha, 0, velocidadfondo)
    if(fondojuego.coords(fondoderecha)[1]>2500):
            fondojuego.move(fondoderecha,0,-fondojuego.coords(fondoderecha)[1])
"""
def guardar():

    archivoTxt = open("archivo.txt", "a")
    archivoTxt.write(str(archivo))
    archivoTxt.close()
"""
def cargardatos():
    global archivo,contador1, contadorg1, contadorv1, contadord1

  

    partida= open("archivo.txt", "r")
    contador1=eval(partida.readline())
    print(contador1)
    contadorg1=eval(partida.readline())
    print(contadorg1)
    contadorv1=eval(partida.readline())
    print(contadorv1)
    contadord1=eval(partida.readline())
    print(contadord1)

    lvl1()

    partida.close()
    

    

    
  
           


    
    


    
    
  
#################
v1=0                             #
v2=0                               #
v3=0                                  #
F=0                                       #
                                                # Parámetros de inicialización

imagenizquierda=mari        # 
imagenderecha=mard      #
velocity=0                       #
#################

#tiempo en etiquetas del jugador 1
contador1=60
tiempojugador1=tkinter.StringVar()

#Gasolina en etiquetas del jugador 1

contadorg1=7000
gasolinajugador1=tkinter.StringVar()

#Velocidad en etiquetas del jugador 1

contadorv1=0
velocidadjugador1=tkinter.StringVar()

#distancia para el juador 1

contadord1=0
distanciajugador1=tkinter.StringVar()




#llamado de funciones
def principal():

    """
    Esta función se encarga de llamar a todas las funciones antes creadas para que al momento de ser llamada empiecen todos los movimientos y se
    pueda iniciar el juego en el respectivo nivel para el jugador 1
    
    """
    global  imagenizquierda,velocity,tiempo1,contador1,tiempojugador1,contadorg1,contadorv1,velocidadjugador1,contadorg2,contadord1,distanciajugador1, archivo


    if colisionesbor()  :
        crash.play()
        sonidofail.play()
        return 0

    if contador1<=0:
        pygame.mixer.music.load("win.wav")
        pygame.mixer.music.play(2)
        
        boton1 = tkinter.Button(v, text="Felicitaciones: vuelve a abrirme y tendrás acceso al siguiente nivel",command=pasar).place(x=540, y=655)
        return 0
    elif (contadorg1<=0):
        return 0
    
    

    else:
        
        Fighter(F,v2)#F es el movimiento en x, v2 el movimiento en y
        MiniVan(v1)
        
        Runner()
        fondomoving(imagenizquierda,velocity)
        mancha(1)
        charge(4)
        colisionescarros()

        partida=open("archivo.txt","w")
       # lista=partida.readline()
        #partida.close()
        

        if contador1>0:
            
            contador1=contador1-0.015
            partida.write(str(round(contador1)))
            partida.write("\n"+str(round(contadorg1)))
            partida.write("\n"+str(round(contadorv1)))
            partida.write("\n"+str(round(contadord1)))
            

            tiempojugador1.set(round(contador1))

        else:
            partida.write(str(round(contador1)))
            partida.write("\n"+str(round(contadorg1)))
            partida.write("\n"+str(round(contadorv1)))
            partida.write("\n"+str(round(contadord1)))

        if contadorg1>0:

            contadorg1=contadorg1-1

            gasolinajugador1.set(round(contadorg1))
            



        if contadorv1<200:

            contadorv1=contadorv1+0.09
            #archivo["SpeedJugador1"]= round(contadorv1)

            velocidadjugador1.set(round(contadorv1))


        contadord1=contadord1+0.09

        #archivo["DistanceJugador1"]= round(contadord1)
        distanciajugador1.set(round(contadord1))

        

    


        #partida.close()
        #tiempodejuego()

        key()

        
      
        #print(var.set())
        #guardar()
        v.after(15,principal)

# tiempo de jugador 2
contador2=60
tiempojugador2=tkinter.StringVar()


#Gasolina del jugador 2

contadorg2=7000
gasolinajugador2=tkinter.StringVar()

#Velocidad en etiquetas del jugador 2

contadorv2=0
velocidadjugador2=tkinter.StringVar()

#distancia para el juador 2

contadord2=0
distanciajugador2=tkinter.StringVar()


def principal2():

    """
    Esta función se encarga de llamar a todas las funciones antes creadas para que al momento de ser llamada empiecen todos los movimientos y se
    pueda iniciar el juego en el respectivo nivel para el jugador 2
    
    """
    global imagenderecha, velocity, contador2, tiempojugador2,contadorg2,contadorv2

    if  colisionesbor2() :
        crash.play()
        sonidofail.play()
        return 0

    elif   contadorg2<=0:
        return 0

    if contador2<=0:
        boton1 = tkinter.Button(v, text="Felicitaciones: vuelve a abrirme y tendrás acceso al siguiente nivel",command=pasar).place(x=540, y=655)
        return 0
        
           

    else:
            MiniVan2(v1)
            Fighter2(F,v2)#F es el movimiento en x, v2 el movimiento en y
            Runner2()
            fondomoving2(imagenderecha,velocity)
            mancha2(1)
            charge2(4)

            colisionescarros2()
            if contador2>0:

                contador2=contador2-0.015            

                tiempojugador2.set(round(contador2))

            if contadorg2>0:

                contadorg2=contadorg2-1

                gasolinajugador2.set(round(contadorg2))
                key2()
                v.after(15, principal2)
            if contadorv2<200:

                 contadorv2=contadorv2+0.09

                 velocidadjugador2.set(round(contadorv2))

            contadord2=contadord1+0.09
            distanciajugador2.set(round(contadord1))

   

def lvl1():
    """
    En esta función se hará el llamado de la función principal, se darán valores para las funciones que tienen parámetros( los cuales se han creado con el fin de
    controlar totalmente, y especialmente para poder darle dificultad a cada nivel , en este caso, al nivel 1), además se agregan condicionales que paran el juego
    en caso de que el jugador pierda la partida.

    """
    global v1,v2,F,po, imagenizquierda, velocity, nombre, nombrecaja,tiempo1, tiempojugador1, contador1
    musicaMenu.stop()
    pygame.mixer.music.load("nivel1.wav")
    pygame.mixer.music.play()

    fondojuego.delete(moraizq)
    fondojuego.delete(morader)
    fondojuego.delete(tierrizq)
    fondojuego.delete(tierrder)
    fondojuego.delete(roizq)
    fondojuego.delete(roder)
    fondojuego.delete(c2)
    fondojuego.delete(c3)
    fondojuego.delete(c4)
    fondojuego.delete(sizq)
    fondojuego.delete(sder)
    fondojuego.delete(c5)



    #fondojuego.lower(c1)

    labeljugador1=tkinter.Label(v,text=nombre.get(), font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=325)
    labeljugador2=tkinter.Label(v,text=nombre2.get(), font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=325)
    labeltiempo1=tkinter.Label(v,textvariable=tiempojugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=570, y=550)
    labeltiempo2=tkinter.Label(v,textvariable=tiempojugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=765, y=550)
    labelgasolina1=tkinter.Label(v,textvariable=gasolinajugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=570, y=450)
    labelgasolina2=tkinter.Label(v,textvariable=gasolinajugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=770, y=450)
    labelvelocidad1=tkinter.Label(v,textvariable=velocidadjugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=570, y=390)
    labelvelocidad2=tkinter.Label(v,textvariable=velocidadjugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=390)
    labeldistancia1=tkinter.Label(v,textvariable=distanciajugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=607)
    labeldistancia2=tkinter.Label(v,textvariable=distanciajugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=607)   
    fondojuego.focus_set()
    
    
    v.deiconify()
    ventana.iconify()
    v1=2
    v2=2#F es el movimiento en x, v2 el movimiento en y, v1 el movimiento vertical de la van
    F=1
    velocity=10


    principal()
    principal2()

    


    


v.iconify()
boton2=tkinter.Button(ventana, image=imagen_2boton,command=lvl1).place(x=1200, y=300)

def lvl2():
    """
    En esta función se hará el llamado de la función principal, se darán valores para las funciones que tienen parámetros( los cuales se han creado con el fin de
    controlar totalmente, y especialmente para poder darle dificultad a cada nivel , en este caso, al nivel 2), además se agregan condicionales que paran el juego
    en caso de que el jugador pierda la partida.

    """
    global v1,v2,F, imagenizquierda, velocity, imagenderecha, tiempojugador1, contador1, velocidadfondo
    musicaMenu.stop()

    pygame.mixer.music.load("nivel2.wav")#canción del nivel 2
    pygame.mixer.music.play()#reproduce la canción del nivel2

    velocidadfondo=20
    fondojuego.delete(moraizq)
    fondojuego.delete(morader)
    fondojuego.delete(roizq)
    fondojuego.delete(roder)
    fondojuego.delete(c1)
    fondojuego.delete(c3)
    fondojuego.delete(c4)
    fondojuego.delete(sizq)
    fondojuego.delete(sder)
    fondojuego.delete(c5)
    labeljugador1=tkinter.Label(v,text=nombre.get(), font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=540, y=339)
    labeljugador2=tkinter.Label(v,text=nombre2.get(), font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=740, y=339)
    labeltiempo1=tkinter.Label(v,textvariable=tiempojugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=570, y=560)
    labeltiempo2=tkinter.Label(v,textvariable=tiempojugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=765, y=560)
    labelgasolina1=tkinter.Label(v,textvariable=gasolinajugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=480)
    labelgasolina2=tkinter.Label(v,textvariable=gasolinajugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=480)
    labelvelocidad1=tkinter.Label(v,textvariable=velocidadjugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=400) 
    labelvelocidad2=tkinter.Label(v,textvariable=velocidadjugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=400)
    labeldistancia1=tkinter.Label(v,textvariable=distanciajugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=620)
    labeldistancia2=tkinter.Label(v,textvariable=distanciajugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=620)   

    fondojuego.focus_set()
    v.deiconify()
    ventana.iconify()
    v1=4#F es el movimiento en x, v2 el movimiento en y, v1 el movimiento vertical de la van
    v2=3
    F=1.2
    imagenizquierda=tierrizq
    imagenderecha=tierrder
    velocity=13
    principal()
    principal2()

v.iconify()
boton3=tkinter.Button(ventana, image=imagen_3boton,command=lvl2).place(x=1200, y=350)

def lvl3():

    """
    En esta función se hará el llamado de la función principal, se darán valores para las funciones que tienen parámetros( los cuales se han creado con el fin de
    controlar totalmente, y especialmente para poder darle dificultad a cada nivel , en este caso, al nivel 3), además se agregan condicionales que paran el juego
    en caso de que el jugador pierda la partida.

    """
    global v1,v2,F,imagenizquierda, velocity, imagenderecha, tiempojugador1, contador1, velocidadfondo

    musicaMenu.stop()
    pygame.mixer.music.load("nivel3.wav")
    pygame.mixer.music.play()

    velocidadfondo=30

    fondojuego.delete(tierrizq)
    fondojuego.delete(tierrder)
    fondojuego.delete(roizq)
    fondojuego.delete(roder)
    fondojuego.delete(c2)
    fondojuego.delete(c1)
    fondojuego.delete(c4)
    fondojuego.delete(sizq)
    fondojuego.delete(sder)
    fondojuego.delete(c5)
    labeljugador1=tkinter.Label(v,text=nombre.get(), font=("Tempus Sans ITC",20),fg="black",bg="white").place(x=545, y=329)
    labeljugador2=tkinter.Label(v,text=nombre2.get(), font=("Tempus Sans ITC",20),fg="black",bg="white").place(x=745, y=329)
    labeltiempo1=tkinter.Label(v,textvariable=tiempojugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=570, y=550)
    labeltiempo2=tkinter.Label(v,textvariable=tiempojugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=765, y=550)
    labelgasolina1=tkinter.Label(v,textvariable=gasolinajugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=480)
    labelgasolina2=tkinter.Label(v,textvariable=gasolinajugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=480)
    labelvelocidad1=tkinter.Label(v,textvariable=velocidadjugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=565, y=390) 
    labelvelocidad2=tkinter.Label(v,textvariable=velocidadjugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=765, y=390)
    labeldistancia1=tkinter.Label(v,textvariable=distanciajugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=612)
    labeldistancia2=tkinter.Label(v,textvariable=distanciajugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=612)   
    fondojuego.focus_set()
    v.deiconify()
    ventana.iconify()
    v1=5#F es el movimiento en x, v2 el movimiento en y, v1 el movimiento vertical de la van
    v2=4
    F=1.5
    imagenizquierda=moraizq
    imagenderecha=morader
    velocity=15
    principal()
    principal2()
v.iconify()
boton4=tkinter.Button(ventana, image=imagen_4boton,command=lvl3).place(x=1200, y=400)

def lvl4():

     """
     En esta función se hará el llamado de la función principal, se darán valores para las funciones que tienen parámetros( los cuales se han creado con el fin de
     controlar totalmente, y especialmente para poder darle dificultad a cada nivel , en este caso, al nivel 2), además se agregan condicionales que paran el juego
     en caso de que el jugador pierda la partida.

     """
     global  v1,v2,F,imagenizquierda, velocity, imagenderecha, tiempojugador1, contador1, velocidadfondo

     musicaMenu.stop()
     pygame.mixer.music.load("nivel4.wav")
     pygame.mixer.music.play()

     velocidadfondo=40

     fondojuego.delete(sizq)
     fondojuego.delete(sder)
     fondojuego.delete(c5)
     labeljugador1=tkinter.Label(v,text=nombre.get(), font=("Tempus Sans ITC",20),fg="black",bg="white").place(x=540, y=339)
     labeljugador2=tkinter.Label(v,text=nombre2.get(), font=("Tempus Sans ITC",20),fg="black",bg="white").place(x=740, y=339)
     labeltiempo1=tkinter.Label(v,textvariable=tiempojugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=570, y=550)
     labeltiempo2=tkinter.Label(v,textvariable=tiempojugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=765, y=550)
     labelgasolina1=tkinter.Label(v,textvariable=gasolinajugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=460)
     labelgasolina2=tkinter.Label(v,textvariable=gasolinajugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=460)
     labelvelocidad1=tkinter.Label(v,textvariable=velocidadjugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=555, y=387) 
     labelvelocidad2=tkinter.Label(v,textvariable=velocidadjugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=755, y=387)
     labeldistancia1=tkinter.Label(v,textvariable=distanciajugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=607)
     labeldistancia2=tkinter.Label(v,textvariable=distanciajugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=607)   
     fondojuego.focus_set()
     v.deiconify()
     ventana.iconify()
     v1=6
     v2=5#F es el movimiento en x, v2 el movimiento en y, v1 el movimiento vertical de la van
     F=1.6
     velocity=15
     imagenizquierda=roizq
     imagenderecha=roder
     principal()
     principal2()
v.iconify()
boton5=tkinter.Button(ventana, image=imagen_5boton,command=lvl4).place(x=1200, y=450)

def lvl5():

     """
     En esta función se hará el llamado de la función principal, se darán valores para las funciones que tienen parámetros( los cuales se han creado con el fin de
     controlar totalmente, y especialmente para poder darle dificultad a cada nivel , en este caso, al nivel 2), además se agregan condicionales que paran el juego
     en caso de que el jugador pierda la partida.

     """
     global v1,v2,F,imagenizquierda, velocity, imagenderecha, tiempojugador1, contador1,velocidadfondo
     musicaMenu.stop()
     pygame.mixer.music.load("nivel5.wav")
     pygame.mixer.music.play()

     velocidadfondo=50
     
     labeljugador1=tkinter.Label(v,text=nombre.get(), font=("Tempus Sans ITC",20),fg="black",bg="white").place(x=540, y=339)
     labeljugador2=tkinter.Label(v,text=nombre2.get(), font=("Tempus Sans ITC",20),fg="black",bg="white").place(x=740, y=339)
     labeltiempo1=tkinter.Label(v,textvariable=tiempojugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=570, y=550)
     labeltiempo2=tkinter.Label(v,textvariable=tiempojugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=765, y=550)
     labelgasolina1=tkinter.Label(v,textvariable=gasolinajugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=460)
     labelgasolina2=tkinter.Label(v,textvariable=gasolinajugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=460)
     labelvelocidad1=tkinter.Label(v,textvariable=velocidadjugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=387) 
     labelvelocidad2=tkinter.Label(v,textvariable=velocidadjugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=387)   
     labeldistancia1=tkinter.Label(v,textvariable=distanciajugador1, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=560, y=607)
     labeldistancia2=tkinter.Label(v,textvariable=distanciajugador2, font=("Tempus Sans ITC",20),fg="blue",bg="white").place(x=760, y=607)        
     fondojuego.focus_set()
     v.deiconify()
     ventana.iconify()
     v1=7
     v2=8
     F=2#F es el movimiento en x, v2 el movimiento en y, v1 el movimiento vertical de la van
     velocity=16
     imagenizquierda=sizq
     imagenderecha=sder
     principal()
     principal2()
v.iconify()
boton6=tkinter.Button(ventana, image=imagen_6boton,command=lvl5).place(x=1200, y=500)
Continuar=tkinter.Button(ventana,text="Continuar" ,font=("Tempus Sans ITC",12),command=cargardatos).place(x=1200, y=550)


def pasar():
    """
    Esta función permite al usuario pasar al siguiente nivel

    """
    v.destroy()
    ventana.destroy()
    import BodyGame







# Liga el evento key al canvas
fondojuego.bind("<KeyPress>",keydown)
fondojuego.bind("<KeyRelease>",keyup)




#enpaquetado( mostrar lo hecho con canvas)

fondojuego.pack()




#ciclo para escuchar los eventos
v.mainloop()
