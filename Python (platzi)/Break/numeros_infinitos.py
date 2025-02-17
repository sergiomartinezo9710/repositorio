def llenar_lista(cantidad):
  """
  Esta función crea una lista vacía y la llena con valores según la cantidad especificada.

  Args:
    cantidad: Un entero que indica la cantidad de elementos de la lista.

  Returns:
    Una lista con los elementos ingresados por el usuario.
  """

  numeros = []
  for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

  lista_a_llenar = [None] * len(numeros)
  for i in range(len(lista_a_llenar)):
    valor = input(f"Ingrese un valor para la posición {i+1}: ")
    lista_a_llenar[i] = valor

  return lista_a_llenar

# Pedimos al usuario la cantidad de números
n = int(input("Ingrese la cantidad de números: "))

# Llamamos a la función para llenar la lista
resultado = llenar_lista(n)

# Imprimimos la lista resultante
print(resultado)