from tkinter import *

def sumar():
    pass

def restar():
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


ventana.mainloop()
