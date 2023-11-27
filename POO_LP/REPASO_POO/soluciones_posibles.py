class Persona:
    def __init__(self,nombre:str,edad:int,sexo:str):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo

    def comer(self,plato_fav:str):
        return f"yo {self.nombre} estoy comiendo mi {plato_fav}" 

class Estudiante(Persona):
    def __init__(self,nombre:str,edad:int,sexo:str,carrera_profesional:str):
        super().__init__(nombre,edad,sexo)
        self.carrera_profesional=carrera_profesional

    def estudia(self):
        return "Estudia de 8 a.m - 12 m"

class Trabajadores(Persona):
    def __init__(self,nombre:str,edad:int,sexo:str,profesion:str):
        super().__init__(nombre,edad,sexo)
        self.profesion=profesion
        
    def trabaja(self):
        return "trabaja en la muni"



alumno=Estudiante("Jory",25,"M","COMPUTACION",)
print(alumno.nombre,alumno.edad,alumno.sexo,":",alumno.carrera_profesional)
print(alumno.comer("LOMO SALTAO ☺"))
print(alumno.estudia())

trabajador=Trabajadores("Edwin",23,"M","DOCENTE")
print(alumno.comer("POLLO FRITO ☺"))
print(trabajador.nombre,trabajador.edad,":",trabajador.profesion)

