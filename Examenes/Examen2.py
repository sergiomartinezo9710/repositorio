#Examen 2

# Crea una funcion que reciba días, horas, minutos y segundos como "list" y retorne su resultado en milisegundos

def milisegundos (dia = 0, hora = 0, minuto = 0, segundos = 0 ):
    tiempo_final = 0
    hora =+ dia * 24
    minuto =+ hora * 60
    segundos =+ minuto * 60
    tiempo_final =+ segundos * 1000
    print(tiempo_final)
    

milisegundos(2,33,23,12)
