from tkinter import *

seleccion=IntVar()
class Calculadora:

    def suma():
        num1=int(num1_text.get())
        num2=int(num2_text.get())
        resultado = num1 + num2

    def resta():
        num1=int(num1_text.get())
        num2=int(num2_text.get())
        resultado = num1 - num2

    def mult():
        num1=int(num1_text.get())
        num2=int(num2_text.get())
        resultado = num1 * num2

    def divi():
        num1=int(num1_text.get())
        num2=int(num2_text.get())
        resultado = num1 / num2



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

tl=Label(ventana, text="Total")
tl.pack()
text_tl =Entry(ventana)
text_tl.pack()

rb_s=Radiobutton(ventana,text="Suma",value="+",variable=seleccion)
rb_s.pack()
rb_r=Radiobutton(ventana,text="Resta",value="-",variable=seleccion)
rb_r.pack()
rb_m=Radiobutton(ventana,text="Multiplicacion",value="*",variable=seleccion)
rb_m.pack()
rb_d=Radiobutton(ventana,text="Division",value="/",variable=seleccion)
rb_d.pack()


boton_calcular =Button(ventana, text="Calcular", command=Calculadora)
boton_calcular.pack()

ventana.mainloop()