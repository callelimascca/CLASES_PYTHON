class Mercado:
    vende="alimentos"

    def __init__(self,num_puesto,propietario, ubicacion, vende, precio):
        self.num_puesto= num_puesto
        self.propietario=propietario
        self.ubicacion=ubicacion
        self.vende=vende
        self.precio=precio

    def abre(self,hora):

        return f"los puestos abren {hora}"
    
    def venta(self):
        return f" el puesto {self.num_puesto} vende menus ☺"
        
    def cierra(self, cierran):
        return f"los puestos cierran "
    
puestos=Mercado('mechita','chinis','entrada sur','menus','precio de mendigo' )


print(puestos.abre('a las 6:00 a.m.'))
print(puestos.cierra('a las 8:00 p.m.'))