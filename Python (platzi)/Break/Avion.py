#import random

#while True:
 #   cupos=int(input("Cuantos cupos desea apartar?: "))
  #  if cupos==1:

   #     print("Listo !")
    #    break
    ###

# Pedimos al usuario que ingrese 4 números
cantidad_numeros = 4
numeros = []

for i in range(cantidad_numeros):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    numeros.append(numero)

# Creamos una lista vacía con la misma cantidad de elementos
lista_a_llenar = [None] * len(numeros)

# Rellenamos la lista con algún valor (puedes cambiarlo por cualquier otro)
for i in range(len(lista_a_llenar)):
    lista_a_llenar[i] = "Valor en la posición {}".format(i+1)

# Imprimimos la lista resultante
print(lista_a_llenar)