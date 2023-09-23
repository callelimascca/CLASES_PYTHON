# REPASO PYTHON 
## **1. TIPOS DE DATOS:**
## TIPOS DE DATOS PRIMITIVOS
**1.2.** Strings
Corresponden a hileras de al menos un carácter o más, los strings pueden ser delimitados utilizando los caracteres “ ”, ‘ ’, ‘’’ ‘’’, y “”” “””. El uso de los mismos debe realizarse bajo las siguientes situaciones:

- “Se utiliza cuando el string contiene ‘comillas simples’. ”
- ‘Se utiliza cuando el string contiene “comillas dobles”. ’
- ‘’’\tSe utiliza cuando el string inicia por un tab (\t), y finaliza por una nueva linea (\n).\n‘’’
- “””Se utilizan si el string contiene saltos de linea intencionales.“””
- **Booleans:** Compuesto básicamente por dos valores True o False, los cuales internamente se almacenan como 1 y 0, respectivamente, razón por la cual se consideran tipos de datos numéricos.
Ejemplo de strings:
```PYTHON
'a', '100', 'False', "hola" # string  cadena texto
'hola como estas' # cadena larga de strings
100 # este es un tipo de dato numerico entero(int).
2.1 # este es un tipo de dato numerico flotante(float).
False, True # este es un tipo de dato boleano 

```
> 💡
> 
> Entero= 10
> 
> Flotante= 3.14
>
> Boleano= False o True (0,1)
>
> Strings = 'False', "hola", '1000', 'a'

![img](https://3.bp.blogspot.com/-5-giDbL0wB0/W582SCIZbmI/AAAAAAAAAMk/VOi9eWmjRvYjo6wUtS-eMHeXf3X7NWL7QCK4BGAYYCw/s1600/Tipos%2Bde%2BDatos.png)


## **2. VARIABLES:**
Es donde almacenamos nuestro tipo de datos, estos datos pueden cambiar(mutar).

Como crear una variable para almacenar los datos:

**1.** Darle un nombre significativo o relacionado al dato que estamos almacenando. 

**2.** Indicar a que dato esta relacionado -> asignación.

**3.** Indicar el tipo de dato que vamos a almacenar en la variable -> darle el dato a guardar.

**Ejemplo**:
```python
nombre_alumno # nombre de la variable
= #asignación o relacion con la variable y el dato 
"maria" # dato almacenado en la variable.
  ```

## **3. OPERADORES:**

##### **1. OPERADORES ARITMETICOS:**
   - SUMA + 
   - RESTA -
   - MULTIPLICACION *
   - DIVISION /
  
  **EJEMPLO:**
  ```python
#SUMA
suma= 45+12
#RESTA
resta= 3-5
#MULTIPLICACION
multi= 2*4
#DIVISION
divi= 4/5

operación= (45+12+23)/4
op= 15+12+14+13/4 #precedencia de operadores 
  ```
##### **2. OPERADORES DE USO ESPECIAL:**

```python
suma=45+42 # operador suma resultado -> 87
suma="45"+42 # opoerador concatenacion resultado 4542
saludo= "hola"+"mundo" # concatenación (holamundo)
saludo= "hola"+" "+"mundo" # concatenar: hola mundo
saludos= "hola" *2 # holahola
```

## **4. DATOS ESTRUCTURADOS:**

#### **1. LISTAS []:**
Puede almacenar distintos tipos de datos en una lista separados por  una coma(,).

**EJEMPLO:**
```python
lista=["nombre", 10, False]
amigos=["Adan", "Edwin",...]
```

#### **2. OBJETOS {}:**
Al igual que las listas tambien almacenan distintos tipos de datos pero con una orden.
Para almacenar datos en un objeto necesitamos especificar un indice y un valor. clave -> valor.

**EJEMPLO:**
```python
{
    "Nombre":"Maria",
    "Edad": 18,
    "Sexo": "Femenino"
}
```
**3. COMBINACION DE AMBAS ESTRUCTURAS DE DATOS "{}+[]":**
```python
Alumno= {
    "Nombre": "Maria"
    "Edad": 18
    "Amigos": ["Anthony", "Edwin",...], 
    "Direccion": {
        "Departamento": "Ayacucho",
        "Provincia": "Lucanas",
        "Distrito": "Puquio"

    }

}
```
## 5. CONTROLES DEN FLUJO
### DECISIONES
Solo se ejecuta el codigo si cumple la condicion es verdadera,  podemas hacer si la condicion sea falsa se ejeute otro codigo.

**SINTAXIS**

Primero especificar el codigo que ejecutara si cumple una condicion
```PYTHON
if <condicion>:
    ## El codigo que deseamos ejecutar si la condicion es verdad
    print('Ejecuta esto')
## Aqui estamos fuera del if o del si este codigo siemprese ejecutara no depende del if
print('Esto siempre ejecutara')
#---------------------------------------------------------------------
# Si queremos que se ejecute un codigo en caso sea falso
if <condicion falsa>:
    print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
```
**EJEMPLOS**

```PYTHON
if 15>18:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```
```PYTHON
if 15*2==30:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```
```PYTHON
condicion= True
if  condicion:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```
## CICLOS
**EXISTEN  DOS TIPOS**

* Cuando sabemos la cantidad de veses que vamos a repetir algo.
Para este caso existe:
  - **FOR**. Sintaxis despues de la palabra reservada **FOR**  deberemos crear una variable que almacene el numero que iremos intentando.luego tendremos que indicar el rango a intentar a los elementos a intentar (es un ciclo que tiene un determinado ciclo).
```PYTHON
for i in range(1,5):
    print(i)
```
```PYTHON
vocales=['a','e','i','o','u']
for i in vocales:
    print (i)
```
```PYTHON
numeros=['45','12','78','1','2']
for i in numeros:
    print (i)
```
* Cuando no sabemos la cantidad de veses que vamos a repetir algo.
Para eso usamos:

    - **WHILE**: Todas las condiciones que son verdaderas van a permitir que el codigo se ejecute, evalua si la condicion es verdadera (es un ciclo infinito).
```python
condicion= True
while condicion:
    print ("hola")
    texto=input("Ingresa tu nombre o salir para terminar el programa del programa: ")
    if texto == "salir"
    condicion = False
```

## 6. FUNCIONES:
Existen dos tipos de funciones:
1. Funciones propias del lenguaje: Que ya viene creadas e insertadas en python y estan listas para ser usadas. 
Estructura de uso de una funcion:
Tiene nombre seguido de parentesis (), dentro de las parentesis podremos pasarle los datos que necesita la fuincion para ejecutarse


>  💡 
>
>FUNCIONES MAS CONOCIDAS:
>
>**print:** Esta es una funcion que nos sirve para mostrar por consola el dato.
```python
print("hola")
# > Nos muestra el dato por consola
hola
```
>**len**: esta funcion nos permite saber la longitud de una lista o un string.

```python
len ("dato")
print(len([1,2,3,4,5,...]))
```
>**input**: es una funcion que espera que se introduzca la información.
entre parentesis pondremos escribir un mensaje que accion realizara el usuario.
```python 
input("Ingresa la información: ")
```

2. Funciones creadas

Una funcion son mini programas tambien se le conoce como modulos o fragmentos de codigo de uso exclusivo.
funciones propias:
pasos para crear una funcion propia.
1. Hacer uso de la palabra **def**
2. Definir un nombre de una funcion que describa que tarea va a ser realizada.
3. Establecer los parametros que resivira la funcion entre **parentesis ()**.
4. Establecer que valor o dato va a retornar mi funcion con la palabra reservada **return**.
 > OBSERVACIÓNES: Tambien podemos hacer uso de la funcion **print()** para retornar un mensaje en nuestra funcion.
Existen dos tipos de funciones los que no resiven ningun parametro y los que resiven parametros
```python 
def saludo():
  print ("hola mundo")
```
- como hacemos la funcion 
- nombre de la funcion y parentesis.
  
#### Funcion con parametros
```python
def mi_print(texto):
print(texto)

#print ("hola este es mi print de python")
#mi_print("hola este es mi print creado")

def suma (a+b):
  total=a+b
  return total

mi_print(suma(45+12)) # 57

EJEMPLO
```python
lista=[12,34,5,7,78]
mi_print(max(lista))

def mi_max(lista):
  numero_mayor=lista[0]
  for numero in lista:
    if numero > numero_mayor:
      numero_mayor= numero
  return numero_mayor
mi_print(mi_max(lista))
#=================================
lista=[12,34,5,7,78]
mi_print(min(lista))

def mi_min(lista):
  numero_menor=lista[0]
  for numero in lista:
    if numero < numero_menor:
      numero_menor= numero
  return numero_menor
mi_print(mi_min(lista))

```
#### funciones con muchos parametros

```python
def funcion(*muchos_parametros*)
  total=0
  for numero in muchos_parametros:
     total=total + numero
  return total
print(funcion(35,45,29,32,78))

def datos(*args):
    nombre=args[0]
    pellidos=args[1]
    edad=args[2]
    return  f" mi nombre es, {nombre}, {apellido},  y mi edad es {edad}"
print(datos("Jenny", "Calle", "12"))
