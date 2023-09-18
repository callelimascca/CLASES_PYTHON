#### SOLUCIONES OPCIONALES:
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