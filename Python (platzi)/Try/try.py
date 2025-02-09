#Try
#En Python, el bloque try se utiliza para manejar excepciones (errores) de manera controlada. Permite ejecutar un bloque de código que podría generar errores, y si ocurre un error, el programa no se detiene abruptamente. En su lugar, se ejecuta el bloque except, donde puedes manejar el error de forma específica o general.
try:
    numerador = int(input("Ingresa el numerador: "))
    denominador = int(input("Ingresa el denominador: "))
    resultado = numerador / denominador
    print("El resultado es: ", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Debes ingresar números válidos.")

