#Excepciones

try:
  print(Holasoygerman)

except NameError: 
  print("Error de tipo NameError ")

except TypeError:
  print("Error tipo error")

else:
  print("Hola mundo")

finally:  #Siempre se imprimirá sin importar lo que ocurra 
  print("Hola soy german")