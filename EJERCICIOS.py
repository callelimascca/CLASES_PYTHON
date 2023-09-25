## 1. crear un programa que me pida la edad de una persona si la edad es mayor o igual a 18 que me muestre un mensaje "eres mayo de edad" caso contrario que me muestre un mensaje "eres menor de edad"
edad=int(input("ingrese su edad: "))
if edad>=18:
   print("eres mayor de edad :) ")
else:
  print("eres menor de edad :(")
## 2. una tienda comercial desea hacer un descuento del 20%, crear un programa que me determine si el cliente se hace acreedor del descuento teniendo encuenta lo siguiente, si el cliente realiza una compra de igual o mayor a 1000 soles mostrar un mensaje que diga "ganaste el descuento del 20% ahora pagaras <mostrar el totalde la compra menos el descuento>" en caso la compra no supere los 1000 soles entonces mostrar un mensaje que diga "no aplicas al descuento <mostrar el monto de la compra>"
compra=float(input("ingrese el monto de la compra: "))
if compra>=1000:
    descuento=0.20*compra
    total_pagar=compra-descuento
    print(f"""
-----------------------------------------------
  GANASTE EL DESCUENTO DEL 20% AHORA PAGARAS:       
total de la compra  : {compra}
descuento           : {descuento}
total a pagar       : {total_pagar}
-----------------------------------------------
""")
else:
    print(f"""
------------------------------------------
        NO APLICAS AL DESCUENTO
monto de la compra  : {compra}
------------------------------------------
""")
## 3. crear un programa que me pida 5 veces un nombre por cada vez que que lo pida muestre la cantidad de veces que ingreso el nombre.
nombre= input("Ingresa un nombre: ")
for nombre in range(1,6):
  print(nombre)

## 4. crear un programa que me pida un numero y lo evalue con el numero premiado si el numero ingresado es incorrecto el programa seguira pidiendo el numero premiado.
numero=123
while True:
  num=int(input("Ingresa un numero: "))
  if num == numero:
    print("FELICIDADES, HAS GANADO EL PREMIO!! ")
  else:
     print("LO SENTIMOS EL NUMERO INGRESADO NO ES VALIDO, SIGA INTENTANDO.")

## 5. crear una funcion por cada operador aritmetico que reciba dos parametros y que te retorne el resultado de la operacion.

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b
    
def divi(a,b):
    return a/b

def multi(a,b):
    return a*b

def resultados(resultado):
    print(resultado)

resultado_suma= suma(6,3)
resultado_resta= resta(6,3)
resultado_divi= divi(6,3)
resultado_multi= multi(6,3)

resultados(resultado_suma)
resultados(resultado_resta)
resultados(resultado_divi)
resultados(resultado_multi)

## 6. Escribe una funcion que reciba un numero entero positivo y devuelva su factorial

num = int(input('ingresa un numero positivo: '))

def factorial(n):
    if n == 0:
        return 1
    if num < 0: 
        print("error, ingresaste un numero negativo")
    else:
        return n * factorial(n - 1)
result = factorial(num)
print(result)

## 7. escribir una funcion que reciba como parametros una lista de numeros y retorne una nueva lista con el cuadro de cada numero de la lista ingresada
lista_numeros=[2,4,8]
def funcion(lista):
    nueva_lista=[]
    for numero in lista:
        nueva_lista.append(numero**2)
    return nueva_lista
#print(funcion(45,50,15,20))

print(funcion(lista_numeros))


## 8. escribir un programa que reciba una cadena de caracteres y devuelva un objeto con cada palabra que contiene y su frecuencia.

def contar_frecuencia_palabras(cadena):
    frecuencia_palabras = {
       'cadena': '',
       'frecuencia': 0
    }
    palabras = cadena.split()

    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras['cadena'] = palabra
            frecuencia_palabras['frecuencia'] += 1
        else:
            frecuencia_palabras[palabra] = 1

    return frecuencia_palabras

# Ejemplo de uso:
cadena = "Hola mundo, hola de nuevo"
resultado = contar_frecuencia_palabras(cadena)
print(resultado)
