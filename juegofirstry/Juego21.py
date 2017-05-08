# Se crea la ventana principal del juego

import tkinter



    

ventana = tkinter.Tk()
ventana.title("Road Fighter")
ventana.geometry("1890x1000")
# inserto la imagen de fondo que lleva el menú

imagen1 = tkinter.PhotoImage(file="fondoprincipal.png")
fondo = tkinter.Label(ventana, image=imagen1).place(x=0 ,y=0)



#defino función para mi boton de salir
def salir ():
    quit()

#creo función para cuando necesite abrir una ventana dependiendo el numero del jugador
"""def nivel1():

    
        ventana=tkinter.Toplevel()
        ventana.title="Road Fighter Juan José"
        ventana.geometry("1890x1000")
        MiniVan()
       
        

        
        
                

        m= 0


        def MiniVan():
          
            vancar=tkinter.PhotoImage(file="RedCar.png")
            p = canvas.create_image(50,50,image=vancar)
            
            global v,m
            if(m<500):
                canvas.move(p,0,2)
                time.sleep(0.02)
            
                m = m+ 1
                v.after(5,MiniVan)
            
   
        

canvas = tkinter.Canvas(ventana,width=900,height=600)
canvas.pack()
#vancar=tkinter.PhotoImage(file="RedCar.png")
#p = canvas.create_image(50,50,image=vancar)

#MiniVan()
"""


       


# creo los botones de mi menú
#Botones para los 5 niveles
imagen_2boton=tkinter.PhotoImage(file="Level1.png")
boton2=tkinter.Button(ventana, image=imagen_2boton,command=None).place(x=1200, y=300)

imagen_3boton=tkinter.PhotoImage(file="Level2.png")
boton3=tkinter.Button(ventana, image=imagen_3boton).place(x=1200, y=350)

imagen_4boton=tkinter.PhotoImage(file="Level3.png")
boton4=tkinter.Button(ventana, image=imagen_4boton).place(x=1200, y=400)

imagen_5boton=tkinter.PhotoImage(file="Level4.png")
boton5=tkinter.Button(ventana, image=imagen_5boton).place(x=1200, y=450)

imagen_6boton=tkinter.PhotoImage(file="Level5.png")
boton6=tkinter.Button(ventana, image=imagen_6boton).place(x=1200, y=500)





#BotonSalir
imagen_1boton = tkinter.PhotoImage(file="BotonSalir.png")
boton1 = tkinter.Button(ventana, image=imagen_1boton,command=exit).place(x=1200, y=600)

#Doy título a mi Juego

Imagen = tkinter.Label(ventana,text="Road Fighter", font=("Tempus Sans ITC",72)).place(x=450, y=20)

#Creación de botonoes para saber si va a jugar una o dos personas
num=tkinter.IntVar()


rdboton1=tkinter.Radiobutton(ventana,text="  Jugar solo   ",value=1, variable=num).place(x=40, y= 240)
rdboton2=tkinter.Radiobutton(ventana,text="Jugar acompañado",value=2, variable=num).place(x=140, y= 240)



#etiquetas para las entradas de los dos jugadores
nombre= tkinter.Label(ventana,text="Nombre del jugador 1", font=("Tempus Sans ITC",12)).place(x=20, y=395)
nombre2= tkinter.Label(ventana,text="Nombre del jugador 2", font=("Tempus Sans ITC",12)).place(x=20, y=445)

#entradas para los dos jugadores
entrada1 = tkinter.Entry(ventana,font=("Tempus Sans ITC",12)).place(x=180, y = 395)
entrada2 = tkinter.Entry(ventana,font=("Tempus Sans ITC",12)).place(x=180, y = 445)

#etiqueta del desarrollador

desarrollador= tkinter.Label(ventana,text="Desarrollado por: Juan José Hoyos",font=("Arial",10)).place(x=0, y=685)

#Boton de instrucciones del juego

instructions=tkinter.Button(ventana,text="¿Cómo jugar?").place(x=20, y= 500 )









ventana.mainloop()
