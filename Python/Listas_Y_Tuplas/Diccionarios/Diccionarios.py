mi_diccionario = {               #Coleccion de datos que se organizan de par en par
        5:"Sergio",              #Tambien se pueden ultilizar números, simbolos para almacenar datos
        "Apellido":"Martinez",
        "Edad":27
}

print(type(mi_diccionario))
print(mi_diccionario["Apellido"])
print(mi_diccionario[5])

#Sintaxis:

#Acceder a valores y llaves:

print(mi_diccionario["Apellido"])
print(mi_diccionario[5])

print(mi_diccionario.keys())        #Muestra las llaves
print(mi_diccionario.values())      #Muestra los valores 


#Modificar valores:                    

mi_diccionario["Apellido"] = "Ospino"
print(mi_diccionario.values())



#Eliminar Elementos:                 
#del mi_diccionario[5]
mi_diccionario.pop(5)
print(mi_diccionario.keys())         #(Tambien se pueden eliminar solo las llaves o valores)
mi_diccionario.clear()
print(mi_diccionario)



mi_diccionario = {               
        5:"Sergio",             
        "Apellido":"Martinez",
        "Edad":27
}
print(mi_diccionario)


#Comprobar si una clave existe:

print(5 in mi_diccionario)    
print( 4 in mi_diccionario)


        #Iterar sobre un diccionario:

#Iterar sobre claves:
for clave in mi_diccionario:
    print(clave)

#Iterar sobre valores:
for valor in mi_diccionario.values():
    print(valor)


#Iterar sobre claves y valores:      (Imprimir todas las claves y valores )
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")


print(mi_diccionario.items())

#Diccionarios dentro de otros diccionarios:

Diccionario = {

    "diccionario1" : {"Nombre":"Juan", "Edad":25},
    "diccionario2" : {"Nombre":"Ana","Edad":30}
 
}

print(Diccionario["diccionario1"]["Edad"])



mi_diccionario = {
    "persona1": {"nombre": "Juan", "edad": 25},
    "persona2": {"nombre": "Ana", "edad": 30}
}

print(mi_diccionario["persona1"]["nombre"])  # Resultado: Juan
print(mi_diccionario["persona2"]["edad"])  # Resultado: 30
