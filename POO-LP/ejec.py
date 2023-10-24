from tarea import *

class Tiendas_comerciales:
     def tienda_gerente(self, tarea_tiendas,nombre_gerente):
          rpt=list(filter(lambda e:e ["Gerente"]==nombre_gerente,tarea_tiendas))
          return f" Las tiendas pertenecientes a China son:  {rpt}"
     
     def mas_categoria(self, tarea_tiendas):
          rpt= list(filter(lambda el: len(el ["Categoria"]) > 2, tarea_tiendas))
          return f" La(s) o tienda(s) con mayor categorias son: {rpt}"
     
     def ruc_nombre(self,tarea_tiendas):
          rpt=list(map(lambda a:{"RUC":a ["RUC"],"Nombre":a["Nombre"]},tarea_tiendas))
          return  f" los RUC de las tiendas son : {rpt} "
          
     def eliminar_tienda(self,tarea_tiendas, ruc):
          rps=list(filter(lambda e:e ["RUC"] != ruc, tarea_tiendas))
          return f""" La tienda fue eliminado:
==========================================================================
          """
          
     
     def mostrar_todo(self,tarea_tiendas):
          mensaje=f"""
    TIENES {len(tarea_tiendas)} TIENDAS COMERCIALES
    LAS TIENDAS SON: 
    {tarea_tiendas}
"""
          return mensaje
     
rpts=Tiendas_comerciales()
print(rpts.mostrar_todo(tiendas))
print(rpts.tienda_gerente(tiendas, "China"))
print(rpts.mas_categoria(tiendas))
print(rpts.ruc_nombre(tiendas))
print(rpts.eliminar_tienda(tiendas, 2435452))

