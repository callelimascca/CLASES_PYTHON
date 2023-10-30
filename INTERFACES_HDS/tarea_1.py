from tkinter import *

def calcular_promedio():
    
    nota = float(nota_text.get())
    promedio = (nota + float(E_promedio["text"]))/ 4
    E_promedio["text"]= promedio

def limpiar():
    # Limpiar los campos de nota y promedio
    nota_text.delete(0, "end")
    
def eliminar_todo():
    # Limpiar los campos de nota y promedio
    E_promedio["text"] =0
    nota_text.delete(0, "end")
    
def agregar_nota():
    nota = float(nota_text.get())
    promedio = float(E_promedio["text"]) + nota
    E_promedio["text"]= promedio

# Crear la ventana
ventana = Tk()
ventana.title("☻♣◙")

# Crear las etiquetas
notas=Label(ventana, text="Nota")
notas.grid(row=0, column=0)
nota_text =Entry(ventana)
nota_text.grid(row=0, column=1)

promedio_text =Label(ventana, text="Promedio: ")
promedio_text.grid(row=1, column=0)

E_promedio = Label(ventana, text="0")
E_promedio.grid(row=1, column=1)

# Crear los botones
boton_calcular =Button(ventana, text="Calcular", command=calcular_promedio)
boton_calcular.grid(row=2, column=0)
boton_calcular.config(bg="yellow")

boton_limpiar = Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=2, column=1)

boton_agregar = Button(ventana, text="+", command=agregar_nota)
boton_agregar.grid(row=0, column=2)

eliminar = Button(ventana, text="Eliminar", command=eliminar_todo)
eliminar.grid(row=4, column=1)
eliminar.config(bg="red")



ventana.mainloop()