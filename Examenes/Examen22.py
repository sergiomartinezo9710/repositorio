def milisegundos(tiempo):
    dia, hora, minuto, segundos = tiempo
    tiempo_final = 0
    
    # Convertir todo a milisegundos
    tiempo_final += dia * 24 * 60 * 60 * 1000  # Días a milisegundos
    tiempo_final += hora * 60 * 60 * 1000      # Horas a milisegundos
    tiempo_final += minuto * 60 * 1000         # Minutos a milisegundos
    tiempo_final += segundos * 1000            # Segundos a milisegundos
    
    return tiempo_final

# Ejemplo de uso
tiempo = [2, 33, 23, 12]
resultado = milisegundos(tiempo)
print(resultado)


mi_lista = [1,2,3,4,5,]
print(mi_lista.append[-2])