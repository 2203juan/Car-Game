import tkinter
import time

v=tkinter.Tk()
v.geometry("1800x1600")

fondojuego=tkinter.Canvas(v, width=1350, height=700,bd=0,highlightthickness=0)
i=0
z=0



photo=tkinter.PhotoImage(file="Tryfontmove.png")
p=fondojuego.create_image(900,200, image=photo)





def RunnerCar():
  
    

    for i in range(0,550):
                    fondojuego.move(p,0,5)
                    v.update()
                

        
    if(fondojuego.coords(p)[1]>800):
        fondojuego.move(p,0,-800)
        v.update()
        

  

                    
             
                 
                 

                
              


fondojuego.focus_set()
v.after(5,RunnerCar)

fondojuego.pack()


v.mainloop()
