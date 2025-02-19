#Clases

class unHumano: 
  def __init__(self,altura, edad, peso):
    self.altura = altura
    self.edad = edad
    self.peso123 = peso

  def comer(self):
    print(f"el humano de {self.edad} años está comiendo.")          #Error de espacio entre las comillas y los parentesis f 


humano_1 = unHumano(1.80,23,87)
humano_1.comer()



print(f'El humano 1 mide "{humano_1.altura}, pesa {humano_1.peso123} kg, y tiene {humano_1.edad} años')