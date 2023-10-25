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
