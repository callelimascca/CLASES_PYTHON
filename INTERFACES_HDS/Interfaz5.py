# from tkinter import * # * sirve para importar todos las herramientas de tk

# def captura_dato():
#     text=int(texto_nombre.get())
#     mensaje= Label(ventana,text= f"hola,{text}")
#     mensaje.pack()

# ventana=Tk()
# ventana.geometry("300x300")
# ventana.title("♠♠♠")

# etiqueta=Label(ventana, text="Introduce tu Edad: ")#.grid(row=0,column=0) # sirve para colocar y ordenar filas y columnas 
# etiqueta.pack()
# texto_nombre=Entry(ventana)
# texto_nombre.config(bg = "blue", fg="yellow") #fg es para cambiar el color de la letra
# texto_nombre.pack()

# boton_capturar=Button(ventana,text="Enviar", command= captura_dato)
# boton_capturar.pack()

# # sirve para colocar y ordenar filas y columnas 
# # pack: apila y enpaqueta las etiquetas (recibe otras propiedades que grid)

# ventana.mainloop() # mantiene la ventana abierta.

from tkinter import*

def comprobar_datos():
    text1=text_usuario.get()
    text2=int(text_contra.get())
    if text1 == usuario and text2==contra:
        mensaje=Label(ventana,text="Bienvenido :)")      
        mensaje.pack()
    else:
        mensaje=Label(ventana,text="El usuario o contraseña son incorrectas.....revisa de nuevo")      
        mensaje.pack()

ventana =Tk()
ventana.title('CORREO😄')
ventana.geometry("300x200")
ventana.config(bg='grey')

usuario="Maria"
contra=7379961

etiqueta1=Label(ventana,text="Usuario")
etiqueta1.pack()

text_usuario=Entry(ventana)
text_usuario.config(bg="black",fg="white")
text_usuario.pack()

etiqueta2=Label(ventana,text="Contraseña")
etiqueta2.pack()

text_contra=Entry(ventana, show="☺")
text_contra.config(bg="black",fg="white")
text_contra.pack()
boton_capturar=Button(ventana,text="Comprovar",command=comprobar_datos)
boton_capturar.pack()

ventana.mainloop()
