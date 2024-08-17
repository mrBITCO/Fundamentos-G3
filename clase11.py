class Calculadora:
    def __init__(self, numero):
        self.resultado = numero


    def suma(self, numero):
        self.resultado += numero

    def resta(self, numero):
        self.resultado -= numero

    def multiplica(self, numero):
        self.resultado *= numero

    def dividir(self, numero):
        if numero != 0:
         self.resultado /= numero
        else:
           print("Error!: division por cero")

    
    def op_resultado(self):
        return self.resultado 

calculo = Calculadora(0)
 
calculo.suma(587)
calculo.resta(95)
calculo.multiplica(4)
calculo.dividir(0)

ResOperaciones = calculo.op_resultado()
print(ResOperaciones)


"""class Calculadora:
    
    def suma(self, num1, num2):
        return num1 + num2 

    def rersta(self, num1, num2):
        return num1 - num2 
    
    def multi(self, num1, num2):
        return num1 * num2 
    
    def divi(self, num1, num2):
        if num2 == 0: 
            return "Error Division por cero"
        else:
            return num1 / num2
        
calculadora1= Calculadora()

numero1 = float(input("Ingrese un numero1"))
numero2 = float(input("Ingrese numero2"))



print(calculadora1.suma(numero1, numero2))"""




