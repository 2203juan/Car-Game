import tkinter

# Crea la ventana y la asocia a la variable v
v = tkinter.Tk()

presiono = False
x = None
i = 0
j = 0

def derecha():
    """
    """
    global presiono,x,i,j
    d.delete(x)
    i = i + 10
    x = d.create_polygon(100+i,100+j,100+i,200+j,200+i,200+j,200+i,100+j,outline="black",fill="orange")
   # x = d.create_image(100+i,100+j,image=filename)

def izquierda():
    """
    """
    global presiono,x,i,j
    d.delete(x)
    i = i - 10
    x = d.create_polygon(100+i,100+j,100+i,200+j,200+i,200+j,200+i,100+j,outline="black",fill="orange")
    #x = d.create_image(100+i,100+j,image=filename2)

def key(event):
    """
    """
    global x,i,j
    tecla = repr(event.char)
    print(tecla)
    if(tecla == "'d'" ):
        if(i < 500):
            d.delete(x)
            i = i + 10
            x = d.create_image(100+i,100+j,image=filename)
        else:
            d.delete(x)
            i = -100
            x = d.create_image(100+i,100+j,image=filename)
    if(tecla == "'a'"):
        if(i > -50):
            d.delete(x)
            i = i - 10
            x = d.create_image(100+i,100+j,image=filename2)
        else:
            d.delete(x)
            x = d.create_image(100+i,100+j,image=filename3)


# Crea los widgets
b1 = tkinter.Button(v,text="->",command=derecha)
c = tkinter.Label(v,text="MoovingCar")
b2 = tkinter.Button(v,text="<-",command=izquierda)
d = tkinter.Canvas(v, width=500, height=500)

# Liga el evento key al canvas
d.bind("<Key>", key)

# Pone el foco en el canvas
d.focus_set()

# Empaqueta (muestra) los widgets
c.pack()
b1.pack()
b2.pack()
d.pack()

# Dibuja algo en el canvas
#d.create_line(0,0,50,50)
x = d.create_polygon(100+i,100+j,100+i,200+j,200+i,200+j,200+i,100+j,outline="black",fill="orange")

# Carga una imagen
filename = tkinter.PhotoImage(file="carro.png")
filename2 = tkinter.PhotoImage(file="carro.png")
filename3 = tkinter.PhotoImage(file="explosion.png")
x = d.create_image(100,100,image=filename)

# Ciclo para escuchar los eventos
v.mainloop()