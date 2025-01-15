"""Strings 

nombre=input("Cual es tu nombre?")
apellido=input("Cual es tu apellido?")
edad=input("Cual es tu edad?")
all_data=nombre+ " "+apellido+ " "+ edad+"."


print("Su información completa es: ", all_data )


 Quote (Frases o recitar con comillas)

quote='Yo soy sergio'
print(quote)

quote2='Ella dijo "Hola"'
print(quote2)
"""
# Formato    1
print("Formato 1:")
print("")

name=input("Cual es tu nombre?")
last_name=input("Cual es tu apellido?")
age=input("Cual es tu edad?")
template="Hola, mi nombre es " + name +" "+ ", mi apellido es "+ last_name + "y mi edad es"+ age
print("Formato 1:  ",template)
print(" ")


# Formato 2
print("Formato 2: ")
print(" ")
template="Hola, mi nombre es {}, mi apellido es {} y mi edad es {}" .format(name,last_name,age)
print("Formato 2:  ",template)

# Formato 3
print("Formato 3:")
print("")
template= f"Hola, mi nombre es {name} , mi apellido es {last_name} y mi edad es {age}"
print("Formato 3:  ",template)



#                              # Ejercicios


print("Este es un formulario para prueba de manejo, necesitaremos sus siguientes datos")
nombre=input("Ingrese su nombre:  ")
apellido=input("Ingrese su apellido:  ")
edad=input("Ingrese su edad:  ")
direccion=input("Ingrese su dirección de domicilio:  ")

template=f"Los datos que ingresó fueron:  "

print(nombre)