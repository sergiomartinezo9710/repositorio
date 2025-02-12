text="Ella sabe python"
print(text[0])                  #Imprime la posición 0
print(text[1])                  #Imprime la posición 1
#print(text[999])
size= len(text)                 
print("Tamaño:  ",size)         #Muestra la cantidad de caracteres
print(text[size-1])             #Imprime el total de caracteres menos el último
print(text[-1])                 #

#Slicing

print(text[0:5])
print(text[10:16])
print(text[0:10])
print(text[5:-1])
print(text[5:])
print(text[:])
print(text[10:16:1])
print(text[10:16:2])
print(text[::2])
