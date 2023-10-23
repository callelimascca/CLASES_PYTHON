from tkinter import * # * sirve para importar todos las herramientas de tk


def evaluar_datos():
    
    usuario=int(input(texto_usuario.get))
    contra=int(input(text_contraseña.get))
    if usuario == "maria" and contra == "2023":
        mensaje= Label(ventana, text= " Bienvenido al programa ☺")
        mensaje.pack()
    else: 
        mensaje= Label(ventana, text= f""" usuario o contraseña es incorrecta
                        intentalo de nuevo""")
        mensaje.pack()
        

ventana=Tk()
ventana.title("♠♠♠")
ventana.geometry("350x200")

etiqueta=Label(ventana, text="USUARIO: ")
etiqueta.pack()
texto_usuario=Entry(ventana)
texto_usuario.config(bg = "blue", fg="yellow") 
etiqueta.pack()


etiqueta2=Label(ventana, text="CONTRASEÑA: ") 
etiqueta2.pack()
text_contraseña=Entry(ventana, show= "*")
text_contraseña.config(bg = "blue", fg="yellow") 
text_contraseña.pack()


boton_evaluar=Button(ventana, text= "Confirmar", command= evaluar_datos)
boton_evaluar.pack()

ventana.mainloop()