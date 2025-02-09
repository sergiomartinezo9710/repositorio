import math

def area_circulo(radio):
  area = math.pi * radio**2
  return area

# Ejemplo de uso:
radio = int(input("Introduzca el radio: "))
resultado = area_circulo(radio)
print("El área del círculo es:", resultado)