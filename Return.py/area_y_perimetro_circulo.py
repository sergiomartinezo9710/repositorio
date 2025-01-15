def area_circulo(radio):
    area = (3.14)*(radio)**2
    return area

def perimetro_circulo(radio):
    perimetro= (2*3.14)*(radio)
    return perimetro



radio=int(input("Introduzca el radio: "))

resultado = area_circulo(radio)
resultado2 = perimetro_circulo(radio)

print("El area es: ", resultado)
print("El perimetro es: ", resultado2)