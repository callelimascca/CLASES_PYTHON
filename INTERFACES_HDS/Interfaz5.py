from tkinter import * # * sirve para importar todos las herramientas de tk


def evaluar_edad():
    edad=int(texto_edad.get())
   
    if edad >= 18:
        mensaje= Label(ventana, text= " eres mayor de edad ☺")
        mensaje.pack()
        
    else:
        mensaje1= Label(ventana, text= " eres menor de edad :(")
        mensaje1.pack()
    

ventana=Tk()
ventana.geometry("300x300")
ventana.title("♠♠♠")

etiqueta=Label(ventana, text="Introduce tu Edad: ")#.grid(row=0,column=0) # sirve para colocar y ordenar filas y columnas 
etiqueta.pack()
texto_edad=Entry(ventana)
texto_edad.config(bg = "blue", fg="yellow") #fg es para cambiar el color de la letra
texto_edad.pack()

boton_evaluar=Button(ventana, text= "Evaluar", command= evaluar_edad)
boton_evaluar.pack()

# sirve para colocar y ordenar filas y columnas 
# pack: apila y enpaqueta las etiquetas (recibe otras propiedades que grid)

ventana.mainloop() # mantiene la ventana abierta.
