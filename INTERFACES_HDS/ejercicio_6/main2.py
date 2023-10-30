from  tkinter import *

class Calculadora:
    def __init__(self):
        self.ventana= Tk()
        self.ventana.title("CALCULADORA")
        self.num1=IntVar()
        self.num2=IntVar()
        self.resultado=IntVar()
        self.operacion= IntVar()


        self.radio_suma=Radiobutton(self.ventana,text="Suma",value="+",variable=self.operacion)
        self.radio_resta=Radiobutton(self.ventana,tex="Resta",value="-",variable=self.operacion)
        self.radio_mult=Radiobutton(self.ventana,text="Multiplicacion",value="*",variable=self.operacion)
        self.radio_divi=Radiobutton(self.ventana,text="Division",value="/",variable=self.operacion)


        self.num1= Entry(self.ventana,textvariable=self.num1)
        self.num2= Entry(self.ventana, textvariable= self.num2)

        self.resultado=Label(self.ventana,textvariable=self.resultado)

        self.boton=Button(self.ventana, text="Calcular", command= self.calcular)

        self.num1.pack()
        self.num2.pack()
        self.radio_suma.pack()
        self.radio_resta.pack()
        self.radio_mult.pack()
        self.radio_divi.pack()
        self.boton.pack()
        self.resultado.pack()

        self.ventana.mainloop()

    def calcular(self):
        num1 = int(self.num1.get())
        num2 = int(self.num2.get())
        operacion = self.operacion.get()

        if operacion == "+":
                 resultado = num1 + num2
        elif operacion == "-":
                resultado = num1 - num2
        elif operacion == "*":
                resultado = num1 * num2
        elif operacion == "/":
                resultado = num1/ num2
        self.resultado.set(resultado)

Calculadora()           
      



