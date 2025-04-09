calificaciones = []
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = calificaciones
    def promedio(self):
        if len(self.calificaciones) != 0:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0
    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)
    def info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}, Promedio: {self.promedio():.2f}"

#funciones auxiliares

def menu():
    print("1. Registrar nuevo estudiante")
    print("2. Agregar calificación a un estudiante")
    print("3. Mostrar información de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir del programa")
    while True:
        op = input("Seleccione una opción: ")
        if op.isdigit() and 1 <= int(op) <= 5:
            return int(op)
        else:
            print("Opción no válida. Intente de nuevo.")

    
    