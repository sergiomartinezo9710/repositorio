numbers = [1,2,3,4,5,6,7,8,9,10]
tasks =["Make a dishes", "play videogames"]
types = [1, True, "Hola"]

print(numbers)
print(type(numbers))


print(tasks)
print(type(tasks))
print(types)
print(type(types))


print(numbers[0])                                                                                           #Imprime la posición 1 de la lista
print(tasks[0])
print(types[0])


text ="Hola"
#text[0] ="W"                                                                                               #Marca error, no es posible modificar los caracteres de una lista

tasks[1] = "Watch platzi courses"
print(tasks)

tasks[0] = "do the dishes"
print(tasks)

#Slicing en listas

print(numbers[:11])                                                                                         #Imprimir HASTA la posicion 3


print(True in types)                                                                                        #imprime si hay un valor especifico en una lista
print("Hola" in types)                                                                                      #Imprime si hay un valor especifico en una lista