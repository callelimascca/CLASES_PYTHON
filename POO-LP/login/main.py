#crear clase para usuario
#metodos: actualizar_edad
#verificar si usario esta registrado 
#validar usuario y password
from bd import *

class User:
    def actualizar_edad(self, f_nacimiento):
        pass

    def usuario_registrado(self,usuario,password):
        return usuario in usuarios 



    def validar(slef,usuario,password):
        return usuario in usuarios and usuario == usuario and password == password
         
        


rpt=User()

print(rpt.usuario_registrado("admin", "1234"))
if User.usuario_registrado("admin","1234"):
    print("EL USUARIO ESTA REGISTRADO")
else:
    print("EL USUARIO NO ESTA REGISTRADO")

 
if rpt.validar("admin","1234"):
    print("BIENVENIDO AL SISTEMA :)")
else:
    print("CREDENCIALES INCORRECTAS :(")


            

