from tkinter import *
def enviar_boton(ventana,valor):
    if valor =="=":
        expression=ventana.caja_operaciones.get().replace("%","/100")
        resultado=eval(expression)
        ventana.caja_operaciones.delete(0,END)
        ventana.caja_operaciones.insert(0,str(resultado))
        ventana.operacion_label.config(text="SOY RESULTADO")
    elif valor == "c":
        ventana.operacion_label.config(text="")
        ventana.caja_operaciones.delete(0,END)
    elif valor== "<":
        print("te borro el ultimo numero o digito ingresado")
    else: 
        pass

    
    #EVAL --> CONVIERTE UN STRING A UNA EXPRESION MATEMATICA 