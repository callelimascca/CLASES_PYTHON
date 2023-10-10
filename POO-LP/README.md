# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
#### Object Orient Programing(POO).

Es un paradigma de programacion
> **PARADIGMA:** Es un modelo, patron o ejemplo a seguir.

**POO**: Es un modelo de como programar.

> **OBJETIVO:** El objetivo es organizar el codigo de manera ques se asemeje a como pensamos en la vida real.

Se basa en objetos y en la POO un objeto es toda entidad que se puede describir atravez  de **atributos** y **funciones** que puede realizar una entidad.

 ```python
 class Celular:
    # atributos de tipo clase que son iguales para todos los objetos que se crean
    familia='smart Phone'
    #artibutos de instancia son atributos propios del objeto creamos una funcion inicializadora
    
    def __init__(self, marca, modelo, imei, nroCelular):
        self.marca=marca
        self.modelo=modelo
        self.imei=imei
        self.nroCelular=nroCelular
        
        #funcionalidades
    def llamar(self,destino):
        return f'llamando a {destino}'
        
#objeto Celular Jory
llamandoJory=Celular('Iphone', 'x5','95743567',) #instanciando mi clase - creando mi objeto celular
    
print(llamandoJory.marca)
    
print(llamandoJory.familia)
    
print(llamandoJory.llamar ('china'))

    # ==========================================================================
llamandoNadine=Celular('basico', 'x5','6354631234',) #instanciando mi clase - creando mi objeto celular
    
print( llamandoNadine.marca)
    
print( llamandoNadine.familia)
    
print( llamandoNadine.llamar ('edwin'))
    
 ```