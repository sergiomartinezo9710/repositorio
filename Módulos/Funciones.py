def sumar_2numeros(numero1,numero2):
    return numero1 + numero2

 
def datos(nombre,apellido,edad):
    print("Hola, tu nombre y apellidos son: ",nombre, " ", apellido, ",Y tu edad es: ",edad)
    return datos




numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo numero: "))


resultado = sumar_2numeros(numero1,numero2)
print(f"El resultado de los 2 numeros sumados es {resultado}")
