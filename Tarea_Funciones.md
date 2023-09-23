# TAREA
##  AVERIGUAR FUNCIONES DE PYTHON MAS USADAS, CON SUS EJEMPLOS PRACTICOS
#### ¿Qué es una función?

Una función no es más que un bloque de código aislado que lleva a cabo una tarea específica.

Las funciones son muy útiles en programación debido a que eliminan los innecesarios y excesivos ¨copia y pega¨ de código a través de un programa.

Si una acción específica es requerida a menudo en tu código, es un buen indicador de la necesidad de escribir una función. Las funciones son para ser reutilizadas.

Las funciones también te ayudan a organizar tu código.

Si bien Python ya proporciona muchas funciones integradas como print() y len(), también puedes definir tus propias funciones para usar en tus proyectos.

Una de las grandes ventajas de usar funciones en tu código es que reduce el número total de líneas de código en tu proyecto.
### Definir una función en Python
#### 1. **DEF**
   
    Sintaxis
    En Python, una definición de función tiene las siguientes características:
   1. La palabra clave def
   2. Un nombre de función
   3. Paréntesis ’()’, y dentro de los paréntesis los parámetros de entrada, aunque los parámetros de entrada sean opcionales.
   4. Dos puntos ’:’
   5. Algún bloque de código para ejecutar
   6. Una sentencia de retorno (opcional)
```python
# función sin parámetros o retorno de valores
def diHola():
  print("Hello!")

diHola()  # llamada a la función, 'Hello!' se muestra en la consola

# función con un parámetro
def holaConNombre(name):
  print("Hello " + name + "!")

holaConNombre("Ada")  # llamada a la función, 'Hello Ada!' se muestra en la consola

# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
  return val1 * val2

multiplica(3, 5)  # muestra 15 en la consola
```
#### 2. **RETURN**: 
   Una función siempre devuelve un valor. La función utiliza la palabra clave *return*  para devolver un valor; si no desea devolver ningún valor, se devolverá el valor predeterminado None.
```python
# esta es una función básica de suma
def suma(a, b):
  return a + b

result = suma(1, 2)
# result = 3
```

#### 3. **Función max():**
max() es una función incorporada en Python 3. Devuelve el elemento más grande en un iterable o el más grande de dos o más argumentos.

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
```

#### 4. **Función min():**
min() es una función incorporada en Python 3. Devuelve el elemento más pequeño en un iterable o el más pequeño de dos o más argumentos.

EJEMPLO:
```Python
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


