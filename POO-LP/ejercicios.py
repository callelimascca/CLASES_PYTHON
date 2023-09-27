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
mi_celular = Celular("Samsung", "Galaxy S20", "Negro")

# Utilizar los métodos del objeto
mi_celular.llamar("123456789")
mi_celular.enviar_mensaje("987654321", "¡Hola! ¿Cómo estás?") 
#=================================================

# 2. Haciendo uso de la POO crear un objeto para la entidad vehiculo.


# 3. Haciendo uso de la POO crear un objeto para la entidad avion.


# 4. Haciendo uso de la POO crear un objeto para un heroe de Dota2.
