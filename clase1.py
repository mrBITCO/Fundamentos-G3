"""numero1=  int(input("ingrese numero1:"))

numero2=  int(input("ingrese numero2:"))

if numero1  > numero2:
 print (f"{numero1} es mayor que {numero2}")

elif numero1 < numero2:
  print(f"{numero2} es mayor que {numero1}")

else: 
  print("los numero son iguales")"""


# ingrese dos variables tipo flotantes altura y peso, la ultima variable es imc altura/peso

"""peso= float (input("ingrese su peso"))
altura= float (input(" ingrese altura"))
imc= peso /(altura*altura)

if imc < 18.5:
    clasificacion= "Peso Bajo"

elif imc >= 18.5 and imc <= 24.9:
    clasificacion= "Peso Normal"

elif imc >= 25 and imc <= 29.9:
    clasificacion= "Sobrepeso"

else:
    clasificacion= "Obesidad"

print (f"su IMC es {imc:.2f}")
print (f"Su clasificacion {clasificacion}")"""





"""numero = [1, 2, 3, 4, 5, 6]

for x in numero:
    print (x)"""

"""texto = "HOLA CARLOS"

for x in texto:
   print (x)"""



"""numeros = [1, 2, 3, 4, 5]
suma = 0
for numero in numeros:
    suma = suma + numero
print(f"la suma de los numeros es:{suma}")"""


"""numeros = [1, 2, 3, 4, 5, 10]
maximo = 0

for numero in numeros:  
  if numero > maximo:
     maximo = numero
print(maximo)"""


"""i = 1

while i <= 10:
    print(i)
    i = i + 1"""


""""numero = int(input("INGRESA NUMERO:"))
suma = 0 

while numero != 0:
    suma = suma + numero 
    numero = int(input("introduce un numero (0 para terminar):"))
print("la suma es:" , suma)  """


#funciones python 

"""def saludar ():
    print("Hola")

saludar()

def sumar(n1, n2):
    print(n1 +n2)
     
sumar(1,2) """


""""def multiplicar (n1):
    print(n1*1000)
multiplicar (10)"""



""""lista = [1,2,3,4,5]

def maximo(lista):
    print(max(lista))

maximo(lista)"""


"""lista = ["andres,juan,pedro,luciana,mateo"]

print(lista)

lista.append("alejo")
print(lista)"""


lista = [3, -1, 5, -7, 2, 3]

def agregar(lista):
    lista.append(10)
    print(lista)
    
agregar(lista)


def remover(lista):
    lista.remove(5)
    print(lista)

remover(lista)


def ordene(lista):
    lista.sort()
    print(lista)

ordene(lista)
