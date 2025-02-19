numeros=[1,2,3,4,5]
numero_buscado=5
intento=1

for numero in numeros:
    if numero ==numero_buscado:
        print("¡Numero encontrado !", numero_buscado)
        break
    else:
        print("Sigo buscando el numero...")