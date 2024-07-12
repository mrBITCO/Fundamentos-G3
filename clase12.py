#herencia y poliforismo

class Dispositivo_Electronico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def encender(self):
        print(f"{self.marca} {self.modelo}Este dispositivo esta encendido")

    
class Telefono(Dispositivo_Electronico):
    def hacer_llamada(self, numero):
        return (f"Telefono llamando {numero}")


class Portatil(Dispositivo_Electronico):
    def abrir_programa(programa):
        return("Portatil abriendo {self.programa}")


telefono = Dispositivo_Electronico("Iphone", "13")
portatil = Dispositivo_Electronico("Lenovo", "45")


print(telefono.marca, telefono.modelo)
print(portatil.marca, portatil.modelo)

