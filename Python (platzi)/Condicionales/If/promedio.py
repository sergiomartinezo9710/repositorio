numero =int(input("Ingresa un numero:  "))
if numero % 2 == 0: 
    print("Es un numero par")

else:
    print("Es un numero impar")



tool=input("Cual es tu herramienta?  ")

if tool=="Candado":
    print("Ponle candado !")

elif tool=="Martillo":
    print("A martillar !")

elif tool=="llave":
    print("Ponle unMa llave !")


else:
    print("No tienes herramientas, compra una")



stock = int(input("Digita el stock: "))
            
if stock >= 100 and stock <= 1000:
    print("El stock es correcto")

else:
    print("El stock es incorrecto")



promedio=int(input("Cual es tu promedio?  "))           #Se debe declarar el tipo de dato al pedir este dato
if promedio<300:
    print("Vas para fuera de la universidad")

elif promedio>=300 and promedio<=379:
    print("Tienes un promedio normal, te mantienes en la U")

elif promedio>=380 and promedio<=499:
    print("Eres un excelente estudiante, te vamos a dar una beca y un semestre en el exterior. Felicidades !! ")

elif promedio==500:
    print("Eres el mejor estudiante que esta universidad ha tenido !")

elif promedio>500:
    print("Error del sistema, nadie tiene ese promedio")
    
else:
    print("Error !")