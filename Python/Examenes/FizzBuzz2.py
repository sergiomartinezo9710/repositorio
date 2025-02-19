
#FIZZBUZZ #3 Escribe una función que muestre por consola los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
#- Múltiplos de 3 por la palabra "fizz".
#- Múltiplos de 5 por la palabra "buzz".
#- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

#Conclusión: El orden del if no importa en qué orden se ponga, siempre se ejecuta igual
def fizzbuzz (): 

    for contador in range(0,100):
        if contador % 3 == 0:
            print("Fizz ")
        elif contador % 5 == 0:
            print("Buzz")
        else:
            print(contador)
        if contador % 3 == 0 and contador % 5 == 0:    #Aqui lo coloqué al final y corrió igual
            print(f"FIZZBUZZ:",{contador}, "!")

fizzbuzz()