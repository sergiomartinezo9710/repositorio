#CRUD:cut,read,update and delete (cortar,leer,actualizar y eliminar)

numbers=[1,2,3,4,5]
print(numbers[1])
numbers[-1]=10                                                          #modifica un valor, en la ultima posición de la lista
print(numbers)


#Append                                                                 Inserta valores en la última posición de una lista

numbers.append(700)                                                     
numbers.append(8)
numbers.append(5)
print(numbers)


#Insert:                                                                Inserta un valor en una posición en específica

numbers.insert(0,500)                                                   
print(numbers)

numbers.insert(1, "Change")
print(numbers)

tasks= ["todo 1", "todo 2", "todo 3"]
nueva_lista= numbers + tasks
print(nueva_lista)

nueva_lista= tasks + numbers                                            #Importa el orden en que se sumen, va imprimiendo en orden
print(nueva_lista)

#Index                                                                  Indica la posición de un valor en una lista

print(nueva_lista.index("todo 2"))

index=nueva_lista.index("todo 2")
nueva_lista[index]="Holiwis"
print(nueva_lista)

#Remove: Elimina un valor de una lista 

nueva_lista.remove("todo 1")
print(nueva_lista)

#Pop: Elimina valor de una lista

nueva_lista.pop()
print(nueva_lista)

nueva_lista.pop(0)
print(nueva_lista)

#Reverse: invierte los valores de una lista

nueva_lista.reverse()
print(nueva_lista)

numeros= [1,5,6,9,2,0,-2]                                               #Tambien incluye los valores negativos
numeros.sort()
print(numeros)

abecedario=["a","x","c","b","z"]
abecedario.sort()
print(abecedario)
