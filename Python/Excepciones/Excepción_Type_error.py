#Excepción TypeError (error de tipo de dato)

try:
  print(Holasoygerman,1)

except ZeroDivisionError:
  print("No se puede dividir entre cero")

except NameError: 
  print("Error tipo NameError ")

except TypeError:
  print("Error tipo error")

else:
  print("Hola mundo")

finally:           #Siempre se imprimirá sin importar lo que ocurra 
>>>>>>> fba10b9b1fded8f84d8f537e6d4f9400c7c2552c
  print("Hola soy german")