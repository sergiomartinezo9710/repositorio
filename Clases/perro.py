class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando!")

# Creamos dos objetos Perro
perro1 = Perro("Firulais", "Labrador")
perro2 = Perro("Toby", "Pastor alemán")

# Llamamos al método ladrar para cada objeto
perro1.ladrar()  # Imprime: Firulais está ladrando!
perro2.ladrar()  # Imprime: Toby está ladrando!