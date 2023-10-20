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


 <OBSERVACION
 #casos de uso
#historia de usuario
#producto ower
#baclog
#mvp
#prototipos de mierda 

# TAREA 
CRAER UNA LISTA CON 10 OBJETOS QUE CONTENGAN LOS DATOS DE LAS TIENDAS COMERCIALES

> EJEMPLO:
 ```python 
 tiendas=[
    {
        "nombre":"mecha",
        "categoria":["abaroteria"],
        "horario":{
            "dia": 7am-12m,
            "tarde":2pm-8pm
        }

        "gerente": "manuela"

           }
]
```
### observacion:  categorias seran 4
### OBSERVACION: Los gerente seran los siguiente: Edwin, Cristian, Nadine, China
## realizar los siguiente ejercicios:
1. crear un metodo que filtre las tiendas que tienen cada gerente.
2. crear un metodo que se muestre los negocios que tienen mas de dos categorias. **(1 y 2 con lambda)**
3. crear un metodo que me muestre solo el nombre de las tiendas y ruc. **(hacer con map)**

crear una clase para las siguientes metodos o casos de uso.
