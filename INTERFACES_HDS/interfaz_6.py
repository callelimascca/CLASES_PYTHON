from tkinter import *

#instanciamos nuestra clase Tk()
ventana=Tk() #clase para crear una ventana
ventana.title("clase radiobutton") #haciendo uso del metodo title para el titulo
ventana.geometry("400x300")#haciendo uso del metodo geometry para asignar tamaño a la ventana.

#instanciar la clase Label 
etiqueta=Label(ventana, text="radio buttons") #clase para crear una etiqueta 
etiqueta.config(fg="blue",font=50)
#indicar la parte de mi venta que deseo que se muestre (se puede usar grid o pack)
etiqueta.pack()

#instanciar la clase Radiobutton
rb_m=Radiobutton(ventana,text="MASCULINO",value=1)
rb_m.pack()
rb_f=Radiobutton(ventana,text="FEMENINO",value=0)
rb_f.pack()

#llamar metodo de tkinter, permite tener percistencia al mostrar la ventana

ventana.mainloop()