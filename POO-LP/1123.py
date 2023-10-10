#Crear un objeto clase laptop con dos atributos de clase y 5 atributos de instancia debera tener hasta 3 funcionalidades como minim.
#crear tres objetos instancia de clase distinta
class Laptop:
    familia="computadora portatil"
    def __init__(self, marca, modelo,procesador,memoria_ram,almacenamiento):
        self.marca=marca
        self.modelo=modelo
        self.procesador=procesador
        self.memori_ram=memoria_ram
        self.almacenamiento=almacenamiento
    
    def encender(self, endendido):
        return f'la laptop se esta encendiendo........ {endendido}'
    
    def apagar(self, apagada):
        return f'la laptop esta {apagada} '
    
    def info(self):
        return f'la laptop de{self.marca} nos muestra la informacion que ingresamos a la laptop'
    

mi_laptop= Laptop('hp','Pavilion 15-eg0500la','Procesador Intel® Core™ i5 de 11.ª generación', '8MB','Unidad de estado sólido PCIe® NVMe™ M.2 de 256 GB')

print( mi_laptop.encender('la laptop ya esta encendida ☺'))
print( mi_laptop.apagar('apagada ♥'))
print(mi_laptop.info ())

mi_laptop2= Laptop('lenovo','Pavilion 15-eg0500la','Procesador Intel® Core™ i5 de 11.ª generación', '8MB','Unidad de estado sólido PCIe® NVMe™ M.2 de 256 GB')

print( mi_laptop.encender('la laptop ya esta encendida ☺'))
print( mi_laptop.apagar('apagada ♥'))
print(mi_laptop.info ())

mi_laptop3= Laptop('asu','Pavilion 15-eg0500la','Procesador Intel® Core™ i5 de 11.ª generación', '8MB','Unidad de estado sólido PCIe® NVMe™ M.2 de 256 GB')

print( mi_laptop.encender('la laptop ya esta encendida ☺'))
print( mi_laptop.apagar('apagada ♥'))
print(mi_laptop.info ())