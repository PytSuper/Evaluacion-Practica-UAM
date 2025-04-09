import modulo

estudiantes = []

while True:
    op = modulo.menu()
    match op:
        case 1:
            print("\nRegistrar nuevo estudiante:")
            nombre = input("Nombre: ")
            edad = (input("Edad: "))
            carrera = input("Carrera: ")
            estudiantes.append(modulo.Estudiante(nombre, edad, carrera))
            print(f"Estudiante {nombre} registrado exitosamente!\n")

        case 2:
            print("\nAgregar calificación a un estudiante:")
            nombre = input("Nombre del estudiante: ")
            for estudiante in estudiantes:
                if estudiante.nombre == nombre:
                    calificacion = float(input("Ingrese la calificación: "))
                    estudiante.agregar_calificacion(calificacion)
                    print(f"Calificación {calificacion} agregada a {nombre}\n")
                    break
            else:
                print("Estudiante no encontrado\n")

        case 3:
            print("Mostrar información de un estudiante:")
            nombre = input("Nombre del estudiante: ")
            for estudiante in estudiantes:
                if estudiante.nombre == nombre:
                    print(estudiante.info() + "\n")
                    break
            else:
                print("Estudiante no encontrado\n")

        case 4:
            print("\nLista de estudiantes:")
            for estudiante in estudiantes:
                print(estudiante.info())
            print()

        case 5:
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida. Intente de nuevo.\n")
