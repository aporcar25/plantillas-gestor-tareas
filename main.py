from tareas import anadir_tarea, listar_tareas, eliminar_tarea, completar_tarea


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Marcar tarea como completada")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            descripcion = input("Descripción: ").strip()

            if not descripcion:
                print("La tarea no puede estar vacía.")
            else:
                anadir_tarea(descripcion)
                print("Tarea añadida.")


        elif opcion == "2":
            tareas = listar_tareas()
            if not tareas:
                print("No hay tareas.")
            for i, t in enumerate(tareas, start=1):
                estado = "x" if t["completada"] else " "
                print(f"{i}. [{estado}] {t['descripcion']}")
        elif opcion == "3":
            try:
                numero = int(input("Número de tarea: "))
                eliminar_tarea(numero)
                print("Tarea eliminada.")
            except ValueError:
                print("Error: debes introducir un número.")
            except IndexError:
                print("Error: no existe ninguna tarea con ese número.")
        elif opcion == "4":
            numero = int(input("Número de tarea: "))
            completar_tarea(numero)
            print("Tarea marcada como completada.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()