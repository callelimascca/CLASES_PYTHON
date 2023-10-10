class mercado:
    venta="alimentos y otros..."

    def __init__ (self,nom_puesto, propietario, productos, precios, horario):
        self.nom_puesto=nom_puesto
        self.propietario=propietario
        self.productos=productos
        self.precios=precios
        self.horario=horario

    def info(self):
        print(f"""
     +-------------------------------------------------------------+   
     |   Nombre del puesto: {self.nom_puesto}                  
     |   Propietario: {self.propietario}                           
     |   Productos: {self.productos}                           
     |   Precios: {self.precios}                           
     |   Horario de atención: {self.horario}                       
     +--------------------------------------------------------------+   
        """)
    def abre (self, hora):
        return f"""

        el puesto {self.nom_puesto} abre a las {hora}
        """
puesto_China= mercado("la china","lulu","menus","precio regalado","6-7")
print(puesto_China.info())
print(puesto_China.abre("a las 6:30 a.m  :)"))

puesto_uvita= mercado("la uvita","ana","licuados","precio regalado","7-7")
print(puesto_uvita.info())
print(puesto_uvita.abre("a las 7:00 a.m  :)"))

puesto_jory= mercado("la china","jory","frutas","precio regalado","8-5")
print(puesto_jory.info())
print(puesto_jory.abre("a las 8:00 a.m  :)"))
