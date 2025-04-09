import modulo

op = modulo.menu()
match op:
        case 1:
            print("Registrar nuevo estudiante:")

        case 2:
            print("Agregar calificación a un estudiante:")

        case 3:
            print("Mostrar información de un estudiante:")

        case 4:
            print("Lista de estudiantes:")

        case _:
            print("Opción no válida. Intente de nuevo.")
            modulo.menu()
