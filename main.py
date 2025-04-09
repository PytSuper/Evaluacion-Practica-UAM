import modulo
"""Este programa permite gestionar un sistema de estudiantes mediante un menú
 interactivo. Los usuarios pueden registrar nuevos estudiantes, agregar 
 calificaciones, mostrar información de un estudiante específico, listar 
 todos los estudiantes registrados y salir del programa. La información de
   cada estudiante incluye su nombre, edad, carrera, calificaciones y 
   el promedio de estas. El programa utiliza una clase Estudiante para
     modelar a los estudiantes, con métodos para agregar calificaciones,
       calcular el promedio y mostrar la información. Además, valida las
         entradas del usuario, como la edad y las calificaciones, para 
         garantizar que sean correctas."""
estudiantes = []

while True:
    op = modulo.menu()
    match op:
        case 1:
            print("\nRegistrar nuevo estudiante:")
            nombre = input("Nombre: ")
            while True:
                edad = input("Edad: ")
                if edad.isdigit() and int(edad) > 0:
                    edad = int(edad)
                    break
                else:
                    print("La edad debe ser un número positivo.")
            carrera = input("Carrera: ")
            estudiantes.append(modulo.Estudiante(nombre, edad, carrera))
            print(f"Estudiante {nombre} registrado exitosamente!\n")

        case 2:
            print("\nAgregar calificación a un estudiante:")
            nombre = input("Nombre del estudiante: ")
            for estudiante in estudiantes:
                if estudiante.nombre == nombre:
                    calificacion = input("Ingrese la calificación: ")
                    if calificacion.isdigit() and 0 <= float(calificacion) <= 100:
                        estudiante.agregar_calificacion(float(calificacion))
                        print(f"Calificación {calificacion} agregada a {nombre}\n")
                    else:
                        print("La calificación debe ser un número entre 0 y 100.\n")
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
