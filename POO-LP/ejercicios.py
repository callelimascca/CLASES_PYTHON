# 1. Haciendo uso de la POO crear un objeto para la entidad celular.

class Celular:
    marca="Samsung"
    color="negro"
    modelo="Galaxy S20"
    numero= 75634534
    def llamar(self, numero):
        print(f"Llamando al número {numero} desde un celular {Celular.marca} {Celular.modelo} de color {Celular.color}.")

    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje a {numero} desde un celular {Celular.marca} {Celular.modelo} de color {self.color}: {mensaje}.")

    # Crear una instancia de Celular
mi_celular = Celular()

# Utilizar los métodos del objeto
mi_celular.llamar("123456789")
mi_celular.enviar_mensaje("987654321", "¡Hola! ¿Cómo estás?") 
#=================================================

# 2. Haciendo uso de la POO crear un objeto para la entidad vehiculo.
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"El vehículo {self.marca} {self.modelo} está acelerando")

    def frenar(self):
        print(f"El vehículo {self.marca} {self.modelo} está frenando")
mi_vehiculo = Vehiculo("Toyota", "Corolla", "Rojo")

# Acceder a los atributos del objeto
print(f"Marca: {mi_vehiculo.marca}")
print(f"Modelo: {mi_vehiculo.modelo}")
print(f"Color: {mi_vehiculo.color}")
mi_vehiculo.acelerar()
mi_vehiculo.frenar()

# 3. Haciendo uso de la POO crear un objeto para la entidad avion.
class avion: 
    marca='Boeing'
    propietario='L.M'
    color='blanco'
    serie='Boeing-865'

    def despegar(self, km): 
        velocidad= f"vas a {km}km/h de velocidad"
        return velocidad
    def aterrizar(self,):   
        return "aterrisaste"
    def girar(self, direcc):
        direccion=f"giraste hacia la {direcc}."
        return direccion

re=avion()
print(re.marca)
print(re.despegar(120))
print(re.aterrizar())
print(re.girar("izquierda"))

# 4. Haciendo uso de la POO crear un objeto para un heroe de Dota2.
class HeroeDota2: 
    nombre='Invoker'
    daño='daño: 0.96'
    vida='vida: 460'
    regeneracion_vida='regeneracion de vida: 80'
    armadura='armadura: 0.96'
    velocidad_ataque='velocidad de ataque: 285'
    mana='cantidad de mana: 216'
    regeneracion_mana='regenracion: 40'
    habilidades='Habilidades: movimiento fantasmal'

    def movimiento_fantasmal(self, duracion, relentizacion, alcance):        
        daño=f'Usaste el ataque << movimiento fantasmal >>, con una duracion de {duracion}, con una relentizacion de {relentizacion} y con un alcance de {alcance}.'
        return daño
    
rpta=HeroeDota2()
print(rpta.nombre)
print(rpta.daño)
print(rpta.vida)
print(rpta.habilidades)

ataque=input('ingresa el ataque: ')
if ataque=='movimiento fantasmal':
    print(rpta.movimiento_fantasmal(60, 55, 450))

# Crear un objeto para el héroe "Invoker"
invoker = HeroeDota2()

# 5. Haciendo uso de la POO crear un objeto para una PC.

class PC:
    marca='HP'
    modelo='Pavilion'
    procesador='Intel Core i7'
    memoria_RAM= "8 GB"

    def mostrar_informacion(self, marca,modelo,procesador, memoria_RAM):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Procesador:", self.procesador)
        print("Memoria RAM:", self.memoria_RAM)

    def mostrar_por_pantalla(self):
        return f"Mostrar la informacion que el usuario accede a la PC."

mi_PC=PC("HP", "Pavilion", "Intel Core i7", "8GB")
mi_PC.mostrar_informacion
print(mi_PC.mostrar_por_pantalla())
    

# 6. Haciendo uso de la POO crear un objeto para una impresora.

# 7. Haciendo uso de la POO crear un objeto para emitir una factura.