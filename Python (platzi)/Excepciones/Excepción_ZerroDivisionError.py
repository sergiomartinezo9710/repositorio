#Excepción ZeroDivisionError      Es un error que aparece cuando sabemos que dará un valor dividido entre cero 

try:
  print(1/0)

except ZeroDivisionError:
  print("No se puede dividir entre cero")

except NameError: 
  print("Error del sistema ")

except TypeError:
  print("Error tipo error")

else:
  print("Hola mundo")

finally:  #Siempre se imprimirá sin importar lo que ocurra 
  print("Hola soy german")