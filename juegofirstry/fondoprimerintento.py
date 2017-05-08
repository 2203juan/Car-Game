import tkinter
v=tkinter.Tk()
v.geometry("1890x1000")

font= tkinter.PhotoImage(file="Tryfont1.png")
fondojuego=tkinter.Canvas(v, width=1350, height=700,bd=0,highlightthickness=0)
fondomov=fondojuego.create_image(v,500,600,image=font)
myCanvas.pack()

v.mainloop()
