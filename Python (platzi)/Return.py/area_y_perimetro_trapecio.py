def area_trapecio(base_mayor,base_menor,altura):    #Se tienen que llamar la misma cantidad de variables en las funciones
    area = ((base_mayor + base_menor) * altura ) /2
    return area

def perimetro(base_mayor,base_menor):
    perimetro = base_mayor + base_menor + 2
    return perimetro


base_mayor= int(input("Introduzca base mayor: " ))
base_menor = int(input("Introduzca base menor: "))
altura= int(input("Introduzca altura: "))


resultado = area_trapecio(base_mayor,base_menor,altura)   #Se tienen que llamar la misma cantidad de variables en las funciones
resultado2 = perimetro(base_mayor, base_menor)
print("El area es : ",resultado)
print("El perimetro es: ",resultado2)