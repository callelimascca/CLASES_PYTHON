from tarea import *

class Tiendas_comerciales:


     def mostrar_todo(self,tarea_tiendas):
          mensaje=f"""
    TIENES {len(tarea_tiendas)} TIENDAS COMERCIALES
    LAS TIENDAS SON: 
    {tarea_tiendas}
"""
          return mensaje
     
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
{rps}
          """

     def actualizacion(self,tarea_tiendas):
          actualizar=list(filter(lambda a:{"RUC":a["RUC"],"Nombre":a["Nombre"]},tarea_tiendas))
          return f"SE ACTUALIZO CON EXITO {actualizar} "

     def registrar_tienda(self,ruc,nombre,categoria,horario_atencion,gerente):
          nuevo=len(tiendas) +1
          tienda_nueva={
          "RUC":ruc,
          "Nombre":nombre,
          "Categoria":categoria,
          "Horario_atencion":horario_atencion,
          "Gerente":gerente
          }
          registrar=tiendas.append(tienda_nueva)
          return f""" LA TIENDA SE REGISTRO CON EXITO:
===================================================================================
{tienda_nueva}"""
     
     def actualizar_horario(self, ruc, clave, valor):
          tiendas[ruc -1][clave] = valor 
          return "SE ACTUALIZO"

          #self.horario_atencion = nuevo_horario
          return 
     #otro metodo para crear nuevo producto

    
     
rpts=Tiendas_comerciales()
# print(rpts.mostrar_todo(tiendas))
# print(rpts.tienda_gerente(tiendas, "China"))
# print(rpts.mas_categoria(tiendas))
# print(rpts.ruc_nombre(tiendas))
# print(rpts.eliminar_tienda(tiendas, 5456456))
# print(rpts.actualizacion(tiendas))
print(rpts.registrar_tienda(1237456,"Tienda 11",["Bodega", "farmacia"],{"dia":"7am-12m", "tarde":"2pm-7pm"},"LUNA"))
# print(rpts.mostrar_todo(tiendas))
# print(rpts.actualizar_horario(1,"Horario_atencion",{
#             "dia": "6 am - 11 am",
#             "tarde": "1 pm - 7 pm"
#         }))
# print(rpts.mostrar_todo(tiendas))
