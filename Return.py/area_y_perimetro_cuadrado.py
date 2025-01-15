def area_cuadrado(lado):
    """Calcula el área de un cuadrado."""
    area = lado * lado
    return area

def perimetro_cuadrado(lado):
    """Calcula el perímetro de un cuadrado."""
    perimetro = 4 * lado
    return perimetro

# Pedimos al usuario el lado del cuadrado
lado = int(input("Introduzca el lado del cuadrado: "))

# Calculamos el área y el perímetro
area = area_cuadrado(lado)
perimetro = perimetro_cuadrado(lado)

# Imprimimos los resultados
print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro)