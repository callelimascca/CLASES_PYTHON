#### SOLUCIONES OPCIONALES:
# 2. Una tienda comercial desea hacer un descuento del 20%, crear un programa que me determine si el cliente 
#se hace acreedor del descuento teniendo encuenta los siguientes, si el cliente realiza una compra de igual o mayor 
#a 1000 soles mostrar un mensaje que diga "ganaste el descuento del 20%  ahora pagaras <mostrar el total de la compra menos el descuento"
# en caso de la compra no supere los 1000 soles entonces mostrar un mensaje que diga "no aplicas al descuento <mostrar el monto de la compra>" 

nombre=input("Ingresa el nombre del cliente: ")
monto_de_compra=int(input("INGRESE EL MONTO EN SOLES DE LAS COMPRAS COMPRAR: "))
if monto_de_compra >= 1000 :
    descuento = monto_de_compra * 20/100
    Total_descuento= monto_de_compra - descuento
    print(f"""Felicidades {nombre}
    Ganaste el descuento del 20%  
    Total a pagar: {Total_descuento} soles.
           """)
else:
    print(f"""No aplicas al descuento,
    Total a pagar: {monto_de_compra} soles.
          """)
#nombres={}
#for _ in range(5):
#    nombre = input("Ingresa un nombre: ")
#    if nombre in nombres:
#        nombres[nombre] += 1
#    else:
#        nombres[nombre] = 1
#for nombre, cantidad in nombres.items():
#    print("El nombre", nombre, "se ingreso", cantidad,"veces")
        
#numero=123
#while True:
#  num=int(input("Ingresa un numero: "))
#  if num == numero:
#    print("FELICIDADES, HAS GANADO EL PREMIO!! ")

numero_ganador = 45
condicion=True
while condicion:
    numero_ingresado=int(input("Ingresa un numero: "))
    if numero_ingresado == numero_ganador:
        print("GANASTE")
        condicion=False
    else:
        print("sigue intentando")
