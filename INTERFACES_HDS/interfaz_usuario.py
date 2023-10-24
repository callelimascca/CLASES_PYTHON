from tkinter import*

def eval():
    us=user.get()
    cr=int(contra.get())
    if cr ==2023:
        mensaje=Label(ventana,text=f'''
        Hola usuario {us}, 
        la contraseña es correcta.
        .....................................
        Bienvenido 😁''') 
        mensaje.grid(row=3)
    else:
        mensaje=Label(ventana,text=f'''
        Hola usuario {us}
        la contraseña es incorrecta.
        .....................................
        lo sentimos🙂''') 
        mensaje.grid(row=3)

def limpiar():
    user.delete(0,END)
    contra.delete(0,END)
    user.focus()


           
ventana =Tk()
ventana.title('CORREO😄')
ventana.geometry("300x200")
ventana.config(bg='grey')

widget_dos=Frame()
widget_dos.grid(row='2',column='0')
widget_dos.config(height='30',width='30')
widget_dos.config(bg='grey') 

et=Label(ventana, text="USUARIO ")
et.grid(row=0,column=0)

etiqueta =Label(ventana, text="PASSWORD")
etiqueta.grid(row=1,column=0)

user=Entry(ventana)
user.config(bg='black',fg='white')
user.grid(row=0,column=1)

contra=Entry(ventana,show='*')
contra.config(bg='black',fg='white')
contra.grid(row=1,column=1)

boton=Button(ventana,text='Evaluar',command=eval)
boton.grid(row=3,column=0)
#boton.config(bg='pink')

boton_limpiar=Button(ventana,text='Limpiar',command=limpiar).grid(row=3,column=1) 
#boton_limpiar.config(bg='pink')

ventana.mainloop()
##########################################################################################
def comprobar_datos():
    text1=text_usuario.get()
    text2=int(text_contra.get())
    if text1 == usuario and text2==contra:
        mensaje=Label(ventana,text="Bienvenido :)")      
        mensaje.pack()
    else:
        mensaje=Label(ventana,text="El usuario o contraseña son incorrectas.....revisa de nuevo")      
        mensaje.pack()

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
