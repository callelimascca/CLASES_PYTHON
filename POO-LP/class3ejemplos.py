#crear sistema para gestion de stock de productos

#entidades-> entitis--> la base de datos sobre la que voy a trabajar:
#Averiguar Formas Normales(Nprmalizacion de base de datos).

productos=[
    {
        "ID":1,
        "NOMBRE":"ARROZ",
        "DESCRIPCIÓN":"COSTEÑO COSTAL X 100 K",
        "STOCK":5,
        "UNIDAD":"COSTALES",
        "PRECIO":125,
        "MONEDA":"SOLES"

    }
]

#casos de uso
class Producto:

    #atributos de instancia:
    def __init__(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda

    #creacion de metodos:
    def mostrar_productos(self):
        mensaje=f"""
    Tienes {len(productos)} productos
    Los productos son: 
    {productos}
"""
        return mensaje
        
    def registrar_producto(self):
        nuevo_id=len(productos)+1
        producto_nuevo={
            'id': nuevo_id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'stock': self.stock,
            'unidad':self.unidad,
            'precio': self.precio,
            'moneda':self.moneda

        }
        registro_producto=productos.append(producto_nuevo)
        return f"el siguiente producto se registro exitosamente {producto_nuevo}"
    
    def mostrar_un_producto(self,id):
        producto_buscar=productos[id-1]
        return producto_buscar
    
    def eliminar_producto(self,id):
        producto_eliminado=productos.pop(id-1)
        return f"el siguiente producto fue eliminado {producto_eliminado}"

    def actualizar_producto(self,id):
        actualizacion=productos[id+1]
        return actualizacion
    


prod=Producto('aceite','sol 1L',2,'BOTELLA',10)
print(prod.registrar_producto())
print(prod.actualizar_producto(2))
print(prod.mostrar_productos())
print(prod.mostrar_un_producto(1))
print(prod.eliminar_producto(2))
print(prod.actualizar_producto(2))
print(prod.mostrar_productos())



