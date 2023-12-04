import orm
from Tablas.Productos import Productos
from Tablas.Clientes import Clientes
db=orm.SQLiteORM("tiendita")
db.crear_tabla(Productos)
db.crear_tabla(Clientes)

data={
        "nombre": "ace",
        "precios": 2.5,
        "descripcion": "limpia todo",
        "cantidad": 10
}
db.insertarUno("Productos",data)

data=[ 
    {
    "nombre":"china",
    "dni":567898,
    "celular": 76898990,
    "f_nacimiento":"13/06/2004"
    },
    {
    "nombre":"mochi",
    "dni":6775345,
    "celular": 94654574,
    "f_nacimiento":"13/11/2002"
    }
]

db.insertarVarios("Clientes",data)

dat={"nombre":"maria"}
db.actualizar("Clientes",data,"dni=6775345")
db.eliminar("Clientes","dni=6775345")

print(db.mostrar("Clientes",type="objeto"))
print(db.mostrar("Clientes"))
print(db.mostrar("Clientes",where="dni=567898",type="objeto")) #para filtrar
print(db.mostrar("Clientes",where="nombre LIKE 'mo&'",type="objeto")) 
db.cerrar()