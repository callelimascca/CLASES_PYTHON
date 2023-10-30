from  tkinter import *

class Calculadora:
    def __init__(self):
        self.ventana= Tk()
        self.ventana.title("CALCULADORA")

        self.num1=IntVar()
        self.num2=IntVar()
        self.resultado=IntVar()

        self.dato1= Label(self.ventana,text="Ingresa el numero 1: ")
        self.dato1.grid(row=0, column=0)
        self.text1=Entry(self.ventana,textvariable=self.num1)
        self.text1.grid(row=0, column=1)
        
        self.dato2=Label(self.ventana, text="Ingresa el numero 2: ")
        self.dato2.grid(row=1,column=0)
        self.text2=Entry(self.ventana,textvariable=self.num2)
        self.text2.grid(row=1, column=1)

        self.radio_var=IntVar()
        self.radio_var.set("suma")

        self.radio_suma=Radiobutton(self.ventana,text="Suma",variable=self.radio_var,value="suma")
        self.radio_suma.grid(row=2, column=0)

        self.radio_resta=Radiobutton(self.ventana,tex="Resta",variable=self.radio_var,value="resta")
        self.radio_resta.grid(row=2, column=1)

        self.radio_mult=Radiobutton(self.ventana,text="Multiplicacion",variable=self.radio_var,value="multiplicacion")
        self.radio_mult.grid(row=2,column=2)
        
        self.radio_divi=Radiobutton(self.ventana,text="Division",variable=self.radio_var,value="division")
        self.radio_divi.grid(row=2,column=3)

        self.rpt=Label(self.ventana,text="Resultado: ")
        self.rpt.grid(row=3,column=0)
        self.rpt=Label(self.ventana,textvariable=self.resultado)
        self.rpt.grid(row=3, column=1)

        self.boton_calcular=Button(self.ventana,text="Calcular",command=self.calcular)
        self.boton_calcular.grid(row=4,column=1)

        self.ventana.mainloop()
    def calcular(self):
        num1 =int(self.num1.get())
        num2= int(self.num2.get())
        operacion=self.radio_var.get()

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        else:
            resultado = num1/ num2
        self.resultado.set(str(resultado))

calculadora=Calculadora()

