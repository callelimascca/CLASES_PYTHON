# class Perro:
#     #atributos de clase
#     especie="animal"
#     #atributos de instancia
#     def __init__(self):
#         self.nombre=None
#         self.edad=None
#         #methodos --> funciones o acciones que puede realizar mi clase
#     def ingresar_datos(self,nombre,edad):
#         self.nombre=nombre
#         self.edad=edad

#     def ladrar(self):
#         return "guauuu guauuu..."
# #instanciar una clase, es crear un objeto
# #se instancia almacenando en una variable la clase
# boby=Perro("boby",15) #instanciadno o creando un objeto boby
# print(boby.ladrar())
# boby.ingresar_datos("edwin",14)
# print(boby.especie)
class Mascota:
    def __init__(self):
        self.nombre=None
        self.edad=None
        self.tipo_animal=None
    def hablar(self,sonido):
        return sonido
    
    def datos_mascota(self,nombre,edad,tipo_animal):
        self.nombre=nombre
        self.edad=edad
        self.tipo_animal=tipo_animal

class Perro(Mascota):
    def atacar(self):
        return "ladra y muerde"
class Gato(Mascota):
    pass

perro=Perro()
perro.datos_mascota("boby",14,"perro")
print(perro.hablar("guauuu guauuu..."))
print(perro.atacar())
print(perro.nombre,perro.tipo_animal)

gato=Gato()
gato.datos_mascota("luna",3,"gato")
print(gato.hablar("miauuu miauuu..."))
print(gato.nombre,gato.tipo_animal)