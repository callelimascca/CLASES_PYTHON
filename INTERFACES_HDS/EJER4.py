# from tkinter import *

# ventana=Tk()
# ventana.title('ventana_1♥')
# ventana.geometry('400x500')
# widget_uno=Frame()
# widget_uno.grid(row=0,column=0)
# widget_uno.config(width=400, height=50)

# # widget_uno.config(width=400, height=500)
# # widget_uno.config(bg='white')

# #creacion de etiquetas 
# # etiqueta=Label(ventana, text='HOLA SOY CHINISS ☺')
# # etiqueta.grid(row= 0, column=0)
# # etiqueta.config(bg = "pink")
# etiqueta=Label(ventana, text='INGRESA TU NOMBRE')
# etiqueta.grid(row= 1, column=0)

# #CREACION DE CUADRO DE TEXTOS
# cuadro_text= Entry()
# cuadro_text.grid(row=2,column=0)


# ventana.mainloop()

from tkinter import *
ventana=Tk()
ventana.title('ventana_♥')
ventana.geometry('400x500')

widget_uno=Frame()
widget_uno.grid(row=0,column=0)
widget_uno.config(width=50, height=50)

widget_uno=Frame()
widget_uno.grid(row=1,column=0)
widget_uno.config(width=50, height=50)

widget_uno=Frame()
widget_uno.grid(row=2,column=0)
widget_uno.config(width=50, height=50)

widget_uno=Frame()
widget_uno.grid(row=4,column=1, columnspan=3)
widget_uno.config(width=200, height=250)
widget_uno.config(bg='pink')

#etiquetas

etiqueta=Label(ventana, text='NOMBRE Y APELLIDO: ')
etiqueta.grid(row= 0, column=0)

etiqueta=Label(ventana, text='DNI: ')
etiqueta.grid(row= 1, column=0)

etiqueta=Label(ventana, text='CELULAR: ')
etiqueta.grid(row= 2, column=0)

#CREACION DE CUADRO DE TEXTOS

cuadro_text= Entry()
cuadro_text.grid(row=0,column=1)

cuadro_text= Entry()
cuadro_text.grid(row=1,column=1)

cuadro_text= Entry()
cuadro_text.grid(row=2,column=1)


ventana.mainloop()