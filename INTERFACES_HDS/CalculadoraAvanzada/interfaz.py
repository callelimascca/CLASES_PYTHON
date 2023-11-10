from tkinter import*
from tkinter import font
import config as cons

class InterfazCalculadora(Tk):
    def __init__(self):
        super().__init__()
        self.configura_ventana()
        self.construir_widget()

    def configura_ventana(self):
        self.title("CALCULADORA♥")
        #color de fondo
        self.configure(bg=cons.COLOR_FONDO_NEGRO)
        #que no pueda escalar
        self.resizable(0,0)
        #propiedad para darle transparencia
        self.attributes("-alpha", 0.96)
        #llamar a la funcion centrar ventana
        w,h=370,570
        cons.centrar_ventana(self,w,h)

    def construir_widget(self):
        #etiqueta para mostara la operacion
        self.operacion_label=Label(self,text="",font=("Arial",16),fg=cons.COLOR_TEXTO_NEGRO,bg=cons.COLOR_FONDO_NEGRO,justify="right")
        self.operacion_label.grid(row=0,column=3,padx=10,pady=10)
    
    #caja de operaciones muestra los numeros ingresados
        self.caja_operaciones=Entry(self,width=12,font=("Arial", 40),bd=0,fg=cons.COLOR_TEXTO_NEGRO,bg=cons.COLOR_FONDO_NEGRO,justify="right")
        self.caja_operaciones.grid(row=1,column=0,columnspan=4,padx=10,pady=10)

    #CREANDO BOTONES
    botones=[
        "C","%","<","/",
        "7","8","9","*",
        "4","5","6","-"
        "3","2","1","+",
        "0",".","=",
    ]
    row_ini=2
    col_ini=0
    robot_font=font.Font(family="Roboto",size=16)

    for boton in botones:
        if boton in ["=","*","/","-","+","C","<","%"]:
            color_fondo=cons.COLOR_BOTONES_ESPECIAL_NEGRO
            boton_font=font.Font(size=16,weight="bold")
        else:
            color_fondo=cons.COLOR_BOTONES_NEGRO
            boton_font=robot_font
        if boton == "=":
            Button(self,text=boton,width=11,height=2,bg=color_fondo,fg=cons.COLOR_TEXTO_NEGRO,relief=FLAT,font=boton_font,padx=5,pady=5,bd=0,borderwidth=0,highlightthickness=0,overrelief="flat").grid(row=row_ini,column=col_ini,columnspan=2,pady=5)
            col_ini += 1
        else:
            Button(self,text=boton,width=5,height=2,bg=color_fondo,fg=cons.COLOR_TEXTO_NEGRO,relief=FLAT,font=boton_font,padx=5,pady=5,bd=0,borderwidth=0,highlightthickness=0,overrelief="flat").grid(row=row_ini,column=col_ini,pady=5)
            col_ini += 1
        if col_ini >3:
            col_ini=0
            row_ini+=1

