# Lista de tareas
tareas = []

# funciones del programa
# Agregar tarea


def agregar_tarea(lista):
    # entrada para la tarea:
    nueva_tarea = input("Introduzca la nueva tarea: ")
    # añadir la tarea al final de la lista
    lista.append(nueva_tarea)
    # Informe de tarea añadida
    print("\nLa tarea se añadió correctamente")
    # Imprimir la tarea añadida
    print(f"la tarea añadida fue {nueva_tarea}")
    # Informar el número de tarea
    print(f"La tarea se almacenó en la posición {len(lista)} \n")


def ver_tareas(lista):
    # Condicional que evalúe si algo está en la lista
    # Si hay algo en la lista se presenta
    if lista:
        for indice, valor in enumerate(lista):
            print(f"{indice+1}. {valor}")
    # Si la lista esta vacía avisa de ello
    else:
        print("No hay tareas pendientes.")
    # Mensaje de fin del listado
    print("---FIN DEL LISTADO DE TAREAS---")


def tarea_completada(lista):
    # Llamamos a la función ver_tareas()
    ver_tareas(lista)

    # Entrada para que el usuario introduzca una tarea
    completada = int(
        input("Introduzca el número de la tarea a marcar como completada: "))

    # condicional para marcar tareas como completadas
    if completada > 0 and completada <= len(lista):
        # condicional para evaluar si la tarea ya estaba completada
        # Si la tarea ya esta contemplada...
        if "(completada)" in lista[completada - 1]:
            print("La tarea ya estaba marcada como completada")
        # En cambio, sino esta....
        else:
            lista[completada - 1] = "(completada)" + lista[completada - 1]
            print("Se marcó la tarea como completada")
    # avisar si la opcion elegida es invalidad
    else:
        print("Opción Invalida")


def eliminar_tarea(lista):

    # Si la lista contiene algo
    if lista:
        # llamamos a la función ver_tareas()
        ver_tareas(lista)

        # Entrada para que el usuario introduzca una tarea
        tarea = int(input("Introduzca el número de la tarea que desea eliminar: "))

        # Opción invalidad si la tarea no está en el rango de la lista
        if tarea <= 0 or tarea > len(lista):
            print("Opción invalida")

        # Si la Opción es válida se elimina la tarea
        else:
            del lista[tarea-1]
            print("La tarea fue eliminada exitosamente")

    # Si la lista está vacía se avisa de ello
    else:
        print("No hay tareas")
