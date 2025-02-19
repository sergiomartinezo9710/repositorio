# Clases
class estudiante:
    def __init__(self, promedio_semestral, beneficios, promedio_ponderado, registro):
        self.promedio_semestral = promedio_semestral
        self.beneficios = beneficios
        self.promedio_ponderado = promedio_ponderado
        self.registro = registro

    def datos_estudiante(self):
        print(f"El estudiante tiene su promedio semestral de {self.promedio_semestral}, posee los beneficios de: {self.beneficios}, y tiene un promedio ponderado de {self.promedio_ponderado}. Su registro es {self.registro}")

# Crear instancia del estudiante
estudiante1 = estudiante(3.8, "Almuerzos y refrigerios", 4.2, 5)

# Llamar al método para mostrar los datos del estudiante
estudiante1.datos_estudiante()

# Mostrar un dato específico (ejemplo: promedio semestral)
print(f"El estudiante tiene su promedio semestral de {estudiante1.promedio_semestral}, posee los beneficios de: {estudiante1.beneficios}, y tiene un promedio ponderado de {estudiante1.promedio_ponderado}.")
