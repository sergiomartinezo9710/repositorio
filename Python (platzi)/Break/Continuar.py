while True:
    respuesta = input("¿Quieres continuar? (s/n): ")
    if respuesta.lower() == 'n':                 #.lower-> Convierte las letras en minusculas. Otro tipo de dato los deja igual. 
        print("¡Hasta luego!")
        break   