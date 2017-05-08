import tkinter
import time

v=tkinter.Tk()
v.geometry("1890x1000")

fondojuego1=tkinter.Canvas(v, width=1350, height=700,bd=0,highlightthickness=0)




photopo=tkinter.PhotoImage(file="Tryfont3m.png")
po=fondojuego1.create_image(680,200, image=photopo)



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


v.mainloop()
