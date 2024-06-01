import funciones as fn

# Bucle principal

while True:
    # Menú de acciones
    print("\n **** --- Gestor de tareas // Programa 1 --- ****")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("\n")

    # Entrada de datos
    opcion = input("Selecciona una opción: ")
    print("\n")

    # Menú de opciones
    match opcion:
        case "1":
            fn.agregar_tarea(fn.tareas)

        case "2":
            fn.ver_tareas(fn.tareas)

        case "3":
            fn.tarea_completada(fn.tareas)

        case "4":
            fn.eliminar_tarea(fn.tareas)
        case "5":
            print("Gracias por usar nuestro primer programa \nSaliendo...")
            break
        case _:
            print("Opción invalida")
