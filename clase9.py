"""class pikachu: 
    tipo="Electrico"

    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
      self.nombre=nombre
      self.nivel=nivel
      self.salud=salud
      self.voltaje_max=voltaje_max
      self.amperaje_max=amperaje_max
      self.color=color
    
    def atacar(self):
        print(f"Pikachu ataca y otorga un {self.nivel} de daño")

pikachu_1=pikachu("Pepe", 580, 150, 6, 2, "Amarillo")
pikachu_1.nombre 

"""

class Car:

    def __init__(self, marca, modelo, velocidad_max, precio):
        self.marca = marca 
        self.modelo = modelo
        self.__velocidad_max = velocidad_max
        self.__precio = precio

    def acelerar(self):
        self.__velocidad_max += 10
        print(f"Velocidad aumentada a {self.__velocidad_max}")



Car_1 = Car("Mazda","Cx30", 150, 150000000)

Car_1.acelerar()
