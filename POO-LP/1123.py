class Impresora:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo

    def imprimir(self, documento):
        print("Imprimiendo:", documento)

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Tipo:", self.tipo)


# Crear un objeto para una impresora
mi_impresora = Impresora("Epson", "L355", "Inyección de tinta")

# Mostrar la información de la impresora
mi_impresora.mostrar_informacion()

# Imprimir un documento
mi_impresora.imprimir("MiArchivo.pdf")