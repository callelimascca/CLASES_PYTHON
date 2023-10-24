from tarea import *

class Tiendas_comerciales:

#      def mostrar_todo(self,tarea_tiendas):
#           mensaje=f"""
#     TIENES {len(tarea_tiendas)} TIENDAS COMERCIALES
#     LAS TIENDAS SON: 
#     {tarea_tiendas}
# """
#           return mensaje
      
     def tienda_gerente(self, tarea_tiendas,nombre_gerente):
          rpt=list(filter(lambda e:e ["Gerente"]==nombre_gerente,tarea_tiendas))
          return rpt
     
     def mas_categoria(self, tarea_tiendas):
          rpt= list(filter(lambda el: len(el ["Categoria"]) > 2, tarea_tiendas))
          return rpt
     
     def ruc_nombre(self,tarea_tiendas):
          rpt=list(map(lambda a:{"RUC":a ["RUC"],"Nombre":a["Nombre"]},tarea_tiendas))
          return  f" los RUC de las tiendas son : {rpt} "
     
     def eliminar_negocio(self, tarea_tiendas,ruc):
          eliminar= list(filter(lambda r:r ["RUC"] != ruc, tarea_tiendas))
          return f" La siguiente tienda fue eliminada{eliminar} "

     def actualizar(self, tarea_tiendas,ruc):
          actualizacion= list(filter(lambda obj: obj[ruc]==ruc, tarea_tiendas))

          return actualizacion
     
     #otro metodo para crear nuevo producto
     #metodo para actualizar horario de atencion
    
     
rpts=Tiendas_comerciales()
# print(rpts.mostrar_todo(tiendas))
print(rpts.tienda_gerente(tiendas, "China"))
print(rpts.mas_categoria(tiendas))
print(rpts.ruc_nombre(tiendas))
print(rpts.eliminar_negocio(tiendas,5456456))
print(rpts.actualizar(4546776876,"RUC","CUALQUIER COSA"))
