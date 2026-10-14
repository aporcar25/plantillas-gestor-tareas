tareas = []


def anadir_tarea(descripcion):
    tareas.append({"descripcion": descripcion, "completada": False})


def listar_tareas():
    return tareas


def eliminar_tarea(indice):
    if indice < 1:
        raise IndexError
    tareas.pop(indice - 1)

def completar_tarea(indice):
    tareas[indice - 1]["completada"] = True