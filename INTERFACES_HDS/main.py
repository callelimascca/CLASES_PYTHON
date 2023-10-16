import tkinter as tk
from tkinter import filedialog

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Bloc de notas")

# Definir funciones para los botones
def guardar_archivo():
    archivo = filedialog.asksaveasfile(defaultextension=".txt",
                                       filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo is not None:
        contenido = texto.get(1.0, tk.END)
        archivo.write(contenido)
        archivo.close()

def abrir_archivo():
    archivo = filedialog.askopenfile(defaultextension=".txt",
                                     filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo is not None:
        texto.delete(1.0, tk.END)
        contenido = archivo.read()
        texto.insert(tk.END, contenido)
        archivo.close()

# Crear un menú
menu_principal = tk.Menu(ventana)
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
ventana.config(menu=menu_principal)

# Crear un área de texto
texto = tk.Text(ventana)
texto.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()


