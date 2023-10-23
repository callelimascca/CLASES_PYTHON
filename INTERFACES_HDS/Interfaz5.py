from tkinter import * # * sirve para importar todos las herramientas de tk

def captura_dato():
    text=texto_nombre.get()
    mensaje= Label(ventana,text= f"hola,{text}")
    mensaje.pack()

ventana=Tk()
ventana.geometry("300x300")
ventana.title("♠♠♠")

etiqueta=Label(ventana, text="Introduce tu Nombre: ")#.grid(row=0,column=0) # sirve para colocar y ordenar filas y columnas 
etiqueta.pack()
texto_nombre=Entry(ventana)
texto_nombre.config(bg = "blue", fg="yellow") #fg es para cambiar el color de la letra
texto_nombre.pack()

boton_capturar=Button(ventana,text="Enviar", command= captura_dato)
boton_capturar.pack()

# sirve para colocar y ordenar filas y columnas 
# pack: apila y enpaqueta las etiquetas (recibe otras propiedades que grid)

ventana.mainloop() # mantiene la ventana abierta.
