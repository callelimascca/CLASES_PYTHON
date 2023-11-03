from tkinter import *

root = Tk()
root.title("calculadora")
root.geometry("296x265")
root.resizable(0,0)
#pantalla que muestre los numeros ingresados y el resultado

pantalla=Entry(root, 
               width=22,
               bg="#BCCCBF", #asigna color fondo 
               fg="#EAE6C6", #asigna el color de letra
               borderwidth=0, #tamaño del borde de cuadro de texto
               font=("arial", 15, "bold")) #asigna el tipo y tamaño de letra 
pantalla.pack()
pantalla.grid(row=0,columnspan=4,padx=4,pady=4)

root.mainloop