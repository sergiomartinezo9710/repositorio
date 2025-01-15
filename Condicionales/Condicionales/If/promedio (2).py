
promedio=int(input("Cual es tu promedio?  "))           #Se debe declarar el tipo de dato al pedir este dato
if promedio>=250 and promedio <=299:
    print("Tienes el promedio bajo, acercate a facultad de ingenieria para mejorar tu promedio")


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


   