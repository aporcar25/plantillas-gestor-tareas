import json
import os

ARCHIVO = "tareas.json"

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


def guardar_tareas():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=4)


def cargar_tareas():
    if not os.path.exists(ARCHIVO):
        return
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
    except (json.JSONDecodeError, OSError):
        return
    tareas.clear()
    tareas.extend(datos)