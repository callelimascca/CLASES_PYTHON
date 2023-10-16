from tkinter import *

ventana=Tk()
ventana.title('ventana_1♥')
ventana.geometry('400x500')
widget_uno=Frame()
widget_uno.grid(row=0,column=0)
widget_uno.config(width=400, height=50)

# widget_uno.config(width=400, height=500)
# widget_uno.config(bg='white')

#creacion de etiquetas 
# etiqueta=Label(ventana, text='HOLA SOY CHINISS ☺')
# etiqueta.grid(row= 0, column=0)
# etiqueta.config(bg = "pink")
etiqueta=Label(ventana, text='INGRESA TU NOMBRE')
etiqueta.grid(row= 1, column=0)

#CREACION DE CUADRO DE TEXTOS
cuadro_text= Entry()
cuadro_text.grid(row=2,column=0)


ventana.mainloop()