try:

    valor= int(input("ingresa el valor: "))
    resultado= valor / 0

except ZeroDivisionError:
    print("el resultado siempre será cero"," ")
