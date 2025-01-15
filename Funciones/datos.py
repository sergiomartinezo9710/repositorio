def datos(nombre,apellido,edad):
    print("Hola, tu nombre y apellidos son: ",nombre, " ", apellido, ",Y tu edad es: ",edad)
    return datos

nombre=input("Cual es tu nombre? ")
apellido= input("Cual es apellido? ")
edad=int(input("Cual es tu edad? "))

datos2=datos(nombre,apellido,edad)