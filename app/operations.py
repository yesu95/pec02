from app.colors import *
from app.models import To_do

# --- Define añadir tarea ---

def add_task(task_list):

    print(B + "\n------ CREAR NUEVA TAREA ------\n")

    nombre = input(Y + "Nombre de la tarea: " + RA).strip().capitalize()
    descripcion = input(Y + "Descripción" + RA + " [Opcional]: ").strip()
    prioridad = input(Y + "Prioridad (Alta, Media, Baja)" + RA + " [Opcional]: ").strip().lower()

    if not nombre:
        print(R + "\n■ Error: El nombre no puede estar vacío.")
        return False

    # Mientras no este vacía y no sea una prio del array, pedir de nuevo
    while (prioridad != "") and (prioridad not in ("alta", "media", "baja")):
        print(R + "\n■ Error: Prioridad no válida.\n")
        prioridad = input(Y + "Prioridad (Alta, Media, Baja)" + RA + " [Opcional]: ").strip().lower()

    # Se crea diccionario para los kwargs y se añaden si no están vacíos
    kwargs = {}
    if descripcion:
        kwargs["description"] = descripcion.strip()
    if prioridad:
        kwargs["prioridad"] = prioridad.capitalize()

    nueva_tarea = To_do(
        title=nombre.strip().capitalize(),
        **kwargs
    )

    task_list.append(nueva_tarea)
    print(f"{G}\n☑ Tarea '{nombre}' añadida con éxito.")
    return True


# --- Define mostrar tarea ---

def show_tasks(task_list):
    print(B + "\n------ TAREAS REGISTRADAS ------\n")
    if not task_list:
        print(Y + "No hay tareas registradas." + RA)
    else:
        # Enumera las tareas e imprime con indice
        # indice = numero - task = objeto To_do
        for indice, task in enumerate(task_list, 1):
            print(f"{G}{indice}. {RA}{task}")