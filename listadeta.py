def mostrar_menu():
    print("\nLista de Tareas")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver tareas")
    print("4. Marcar tarea como completada")
    print("5. Salir")

def agregar_tarea(tareas):
    tarea = input("Ingrese la tarea: ").strip()
    if tarea:
        tareas.append({"tarea": tarea, "completada": False})
        print(f"Tarea '{tarea}' agregada.")
    else:
        print("No se ingresó ninguna tarea.")


def eliminar_tarea(tareas):
    ver_tareas(tareas)
    try:
        tarea_eliminada = int(input("Ingrese el número de la tarea a eliminar: "))
        if 0 < tarea_eliminada <= len(tareas):
            removed = tareas.pop(tarea_eliminada - 1)
            print(f"Tarea '{removed}' eliminada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada no válida.")

def ver_tareas(tareas):
    if tareas:
        print("\nTareas pendientes:")
        for idx, tarea in enumerate(tareas, 1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{idx}. {tarea['tarea']} - {estado}")
    else:
        print("No hay tareas pendientes.")

def marcar_completada(tareas):
    ver_tareas(tareas)
    try:
        tarea_completada = int(input("Ingrese el número de la tarea a marcar como completada: "))
        if 0 < tarea_completada <= len(tareas):
            tareas[tarea_completada - 1]["completada"] = True
            print(f"Tarea '{tareas[tarea_completada - 1]['tarea']}' marcada como completada.")
            ver_tareas(tareas)
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada no válida.")


def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Elija una opción (1-4): ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            eliminar_tarea(tareas)
        elif opcion == "3":
            ver_tareas(tareas)
        elif opcion == "4":
            marcar_completada(tareas)
        else:
            print("Opción no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
    main()