#While:


numero = 0

while numero < 10:
    numero +=1
    if numero<5:
        print(numero," ", "Es menor que 5")
    elif numero == 5:
        print(numero," ", "Es igual a 5")
    elif numero >5 and numero<=9:
        print(numero," ","Es mayor a 5 ")
    elif numero == 10:
        print(numero, " ","Llegaste hasta el 10")
        break

print("Programa finalizado")