tareas = []


def anadir_tarea(descripcion):
    tareas.append({"descripcion": descripcion, "completada": False})


def listar_tareas():
    return tareas


def eliminar_tarea(indice):
    tareas.pop(indice - 1)