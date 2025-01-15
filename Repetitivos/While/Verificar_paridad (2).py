def verificar_paridad():
  """Verifica si un número entre 1 y 6 es par o impar."""
  while True:
    try:
      numero = int(input("Ingrese un número entre 1 y 6: "))
      if 1 <= numero <= 6:
        if numero % 2 == 0:
          print("El número es par.")
        else:
          print("El número es impar.")
        break
      else:
        print("Por favor, ingrese un número entre 1 y 6.")
    except ValueError:
      print("Eso no es un número válido. Intente de nuevo.")

verificar_paridad()
