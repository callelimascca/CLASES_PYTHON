from tarea import *

class Tiendas_comerciales:
     def tienda_gerente(self, tarea_tiendas,nombre_gerente):
          rpt=list(filter(lambda e:e ["Gerente"]==nombre_gerente,tarea_tiendas))
          return rpt
     
     def mas_categoria(self, tarea_tiendas):
          rpt= list(filter(lambda el: len(el ["Categoria"]) > 2, tarea_tiendas))
          return rpt
     def ruc_nombre(self):
          rpt=list(map(lambda a:{"RUC":a}))
          return rpt
     def mostrar_todo(self):
          pass
     
gerente=Tiendas_comerciales()
print(gerente.tienda_gerente(tiendas, "China"))
print(gerente.mas_categoria(tiendas))
