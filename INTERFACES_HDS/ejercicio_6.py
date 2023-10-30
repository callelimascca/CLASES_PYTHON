from tkinter import *


class Calculadora:

    def suma(self, num1, num2):
        return num1 + num2


    def resta(self, num1, num2):
           return num1 - num2
       

    def mult(self, num1, num2):
        return num1 * num2


    def divi(self, num1, num2):
        return num1 / num2

ventana=Tk()
ventana.geometry("400x300")
calculadora=Calculadora()

def calcular():
    num1= int(num1_text.get())
    num2=int(num2_text.get())
    if rpts.get() == 1:
        resultado =calculadora.suma(num1,num2)
    elif rpts.get() == 2:
        resultado =calculadora.resta(num1,num2)
    elif rpts.get() == 3:
        resultado =calculadora.mult(num1,num2)
    elif rpts.get() == 4:
        resultado =calculadora.divi(num1,num2)
    else:
        resultado = "operacion no valida"
        
    rpt.config(text= "Resultado: " + str (resultado))
    

num_1=Label(ventana, text="Ingresa un numero")
num_1.grid(row=0,column=0)
num1_text =Entry(ventana)
num1_text.grid(row=1,column=0)

num_2=Label(ventana, text="Ingresa un numero")
num_2.grid(row=2,column=0)
num2_text =Entry(ventana)
num2_text.grid(row=3,column=0)

rpt=Label(ventana, text="Total")
rpt.grid(row=4,column=0)
rpta =Label(ventana,text="0")
rpta.grid(row=4, column= 1)

rpts= IntVar()

rb_s=Radiobutton(ventana,text="Suma",value=1,variable=rpts)
rb_s.grid(row=2,column=1)
rb_r=Radiobutton(ventana,text="Resta",value=2,variable=rpts)
rb_r.grid(row=3,column=1)
rb_m=Radiobutton(ventana,text="Multiplicacion",value=3,variable=rpts)
rb_m.grid(row=4,column=1)
rb_d=Radiobutton(ventana,text="Division",value=4,variable=rpts)
rb_d.grid(row=5,column=1)


boton_calcular =Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=7,column=0)

def limpiar():
    num1_text.delete(0,END)
    num2_text.delete(0,END)
    rpta [rpta] = 0
    num_1.focus()
    
boton_limpiar=Button(ventana,text='Limpiar',command=limpiar).grid(row=7,column=1)

ventana.mainloop()