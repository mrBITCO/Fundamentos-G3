class Dog: 
    especie = "Canine"

    def __init__(self, name, age):
      self.name = name
      self.age = age

    def Bark(self):
       print(f"{self.name}, dice Woof! Woof!")

    def Description(self):
       return f"{self.name} tiene {self.age} años"
    
    def Celebration(self):
       return self.age + 1


Dog_1 = Dog("Tony", 3)
Dog_2 = Dog("Firulay", 5)
print(Dog_1.especie, Dog_1.name, Dog_1.age)
print(Dog_2.especie, Dog_2.name, Dog_2.age)

Dog_1.Bark()
Dog_2.Bark()
print(Dog_1.Description())
print(Dog_2.Description())
print(Dog_1.Celebration())
print(Dog_2.Celebration())
