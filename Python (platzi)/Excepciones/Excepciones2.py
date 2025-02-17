#Excepciones

try:
  print(asdasd)

except ZeroDivisionError:
  print("No se puede dividir entre cero")

except NameError: 
  print("Error de NameError ")

except TypeError:
  print("Error de TypeError")

else:
  print("Hola mundo")

finally:            #Siempre se imprimirá sin importar lo que ocurra 
  print("Hola soy german")



try:
  print(1/0)

except ZeroDivisionError:
  print("No se puede dividir entre cero")

except NameError: 
  print("Error de NameError ")

except TypeError:
  print("Error de TypeError")

else:
  print("Hola mundo")

finally:            #Siempre se imprimirá sin importar lo que ocurra 
  print("Hola soy german")