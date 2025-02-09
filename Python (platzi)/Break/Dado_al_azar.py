import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_aleatorio = random.randint(1, 10)

print("Número aleatorio a adivinar:", numero_aleatorio)

intentos = 1
for numero in numeros:
    print(f"Intento {intentos}: {numero}")
    if numero == numero_aleatorio:
        print("¡Adivinaste!")
        break
    intentos += 1

