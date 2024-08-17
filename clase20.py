contador = 0

cadena = "(()())"

for i in cadena:
    if i == "(":
        contador += 1
    elif i == ")":
        contador -= 1
    if contador < 0:
     break
print(contador == 0)
