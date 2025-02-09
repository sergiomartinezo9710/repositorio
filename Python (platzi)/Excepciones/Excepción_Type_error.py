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
  print("Hola soy german")