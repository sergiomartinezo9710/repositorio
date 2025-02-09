def area_rectangulo(base):
    area = base*altura
    return area

def perimetro_rectangulo(base):
    perimetro=(2*base) + (2*altura)
    return perimetro


base= int(input("Introduzca base: "))
altura= int(input("Introduzca altura: "))

resultado1= area_rectangulo(base)
resultado2= perimetro_rectangulo(base)

print("Su area es: ", resultado1)
print("Su perimetro es: ", resultado2)

    
