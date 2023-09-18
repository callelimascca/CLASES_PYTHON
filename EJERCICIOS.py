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