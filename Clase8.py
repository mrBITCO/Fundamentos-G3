lista = [25, 26, 27, 28, 29]
print (lista[-2])
lista.append(30)
print(lista)


frutas = ("manzanas", "pera", "mango", "kiwi")
print(frutas[-3])
print(frutas[2])

lista_frutas = list(frutas)
print(frutas)
print(lista_frutas)
lista_frutas.append("papaya")
print(lista_frutas)
print(tuple(lista_frutas))



for fruta in lista_frutas:
   print(fruta)


contacto = {"Juan": "12545",
             "juana": "854214", 
             "pedro": "9653214"}

print(contacto["juana"])

contacto["ana"] = "548796"
print(contacto)

del contacto["pedro"]
print(contacto)


for nombre, numero in contacto.items():
   print(f"{nombre}: {numero}")
