from tkinter import*
import time

i=0
z=0
ventana= Tk()
ventana.config(bg="black")
canvas=Canvas(ventana, width=500, height=800)

photo=PhotoImage(file="BlueCar.png")
p=canvas.create_image(50,50, image=photo)

def RunnerCar():
    global  i,z
    while i>=0 and i <=160:
                i=0
                for i in range(40,100):
                    canvas.move(p,6,z)
                    ventana.update()
                    time.sleep(0.01)
                    i=i+0.01
                    z=z+0.001

                for i in range(40,100):
                    canvas.move(p,-6,z)
                    ventana.update()
                    time.sleep(0.01)
                    i=i
                    z=z+0.001
                    
canvas.pack()
RunnerCar()
ventana.mainloop()

                
