class Persona:
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.cargo=None

    def caminar(self,pasos):
        return pasos

    def informacion(self,nombre,apellido,edad,cargo):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.cargo=cargo

class Estudiante(Persona):
    def estudia(self):
        return "Estudia de 8 a.m - 12 m"

class Trabajadores(Persona):
    pass

alumno=Estudiante()
alumno.informacion("Jory","Rodriguez",25,"Estudiante")
print(alumno.nombre,alumno.apellido,":",alumno.cargo)
print(alumno.caminar("camina"))
print(alumno.estudia())

trabajador=Trabajadores()
trabajador.informacion("Edwin","Ramos",23,"trabajador")
print(alumno.caminar("camina"))
print(trabajador.nombre,trabajador.apellido,":",trabajador.cargo)

