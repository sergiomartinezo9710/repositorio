import random

while True:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2

    print("El primer dado cayó en:", dado1)
    print("El segundo dado cayó en:", dado2)
    print("La suma es:", suma)

    if suma == 7 or suma == 11:
        print("¡Ganaste!")
        break
    elif suma == 2 or suma == 3 or suma == 12:
        print("¡Perdiste!")
        break
    else:
        print("Tira de nuevo.")