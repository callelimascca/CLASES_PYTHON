from tkinter import *

seleccion=IntVar()

def calcular():
    n1=int(num1_text.get())
    n2=int(num2_text.get())
    resultado= n1 + n2
    pass


ventana=Tk()
ventana.geometry("400x300")

num_1=Label(ventana, text="Ingresa un numero")
num_1.pack()
num1_text =Entry(ventana)
num1_text.pack()

num_2=Label(ventana, text="Ingresa un numero")
num_2.pack()
num2_text =Entry(ventana)
num2_text.pack()

num_3=Label(ventana, text="Total")
num_3.pack()
num3_text =Entry(ventana)
num3_text.pack()

rb_s=Radiobutton(ventana,text="Suma",value="Sumar",variable=seleccion)
rb_s.pack()
rb_r=Radiobutton(ventana,text="Resta",value="Restar",variable=seleccion)
rb_r.pack()

boton_calcular =Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack()

ventana.mainloop()
