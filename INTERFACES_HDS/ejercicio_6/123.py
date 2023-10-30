from tkinter import *


class Calculadora:

    def sum():
        num1=int(num1_text.get())
        num2=int(num2_text.get())
        resultado = num1 + num2
        resultado = rpt
        return resultado

    def resta():
        num1=int(num1_text.get())
        num2=int(num2_text.get())
        resultado = num1 - num2
        resultado = rpt
        return resultado

    def mult():
        num1=int(num1_text.get())
        num2=int(num2_text.get())
        resultado = num1 * num2
        resultado = rpt
        return resultado

    def divi():
        num1=int(num1_text.get())
        num2=int(num2_text.get())
        resultado = num1 / num2
        resultado = rpt
        return resultado



ventana=Tk()
ventana.geometry("400x300")
seleccion=IntVar()

num_1=Label(ventana, text="Ingresa un numero")
num_1.grid(row=0,column=0)
num1_text =Entry(ventana)
num1_text.grid(row=1,column=0)

num_2=Label(ventana, text="Ingresa un numero")
num_2.grid(row=2,column=0)
num2_text =Entry(ventana)
num2_text.grid(row=3,column=0)

rpt=Label(ventana, text="Resultado")
rpt.grid(row=4,column=0)
text_rpt =Entry(ventana)
text_rpt.grid(row=5,column=0)

rb_s=Radiobutton(ventana,text="Suma",value="suma",variable=Calculadora)
rb_s.grid(row=2,column=1)
rb_r=Radiobutton(ventana,text="Resta",value="resta",variable=Calculadora)
rb_r.grid(row=3,column=1)
rb_m=Radiobutton(ventana,text="Multiplicacion",value="mult",variable=Calculadora)
rb_m.grid(row=4,column=1)
rb_d=Radiobutton(ventana,text="Division",value="divi",variable=Calculadora)
rb_d.grid(row=5,column=1)


boton_calcular =Button(ventana, text="Calcular", command=Calculadora)
boton_calcular.grid(row=7,column=0)

# def limpiar():
#     num_1.delete(0,END)
#     num_2.delete(0,END)
#     tl.delete(0,END)
#     num_1.focus()
# boton_limpiar=Button(ventana,text='Limpiar',command=limpiar).grid(row=7,column=1)

ventana.mainloop()