from app.colors import *
from app.models import To_do
import logging

# --- Función mostrar tareas básica --- 

def tasks(task_list):
    for indice, task in enumerate(task_list, 1):
        print(f"{G}{indice}. {RA}{task}")

# --- Función añadir tarea ---

def add_task(task_list):
    try:
        print(B + "\n------ CREAR NUEVA TAREA ------\n")

        nombre = input(Y + "Nombre de la tarea: " + RA).strip().capitalize()
        
        while nombre == "":
            print(R + "\n■ Error: El nombre no puede estar vacío.\n")
            logging.error("Nombre inválido. Intentando ingresar un nombre vacíos.")
            nombre = input(Y + "Nombre de la tarea: " + RA).strip().capitalize()

        descripcion = input(Y + "Descripción" + RA + " [Opcional]: ").strip()
        prioridad = input(Y + "Prioridad (Alta, Media, Baja)" + RA + " [Opcional]: ").strip().lower()

        # Mientras no este vacía y no sea una prio del array, pedir de nuevo
        while (prioridad != "") and (prioridad not in ("alta", "media", "baja")):
            print(R + "\n■ Error: Prioridad no válida.\n")
            logging.error(f"Prioridad inválida. Intendando ingresar '{prioridad}' como prioridad.")
            prioridad = input(Y + "Prioridad (Alta, Media, Baja)" + RA + " [Opcional]: ").strip().lower()

        kwargs = {}
        if descripcion:
            kwargs["description"] = descripcion
        if prioridad:
            kwargs["prioridad"] = prioridad.capitalize()

        # Se le pasan los argumentos al constructor para hacer un nuevo objeto
        nueva_tarea = To_do(
            title=nombre,
            **kwargs
        )

        task_list.append(nueva_tarea)
        print(f"{G}\n☑ Tarea '{nombre}' añadida con éxito.{RA}")
        logging.info(f"Tarea creada con éxito: {nombre}")

        return True

    except Exception as e:
        print(R + f"\n■ Error al procesar la tarea: {e}{RA}")
        logging.error("Tarea no creada: Ocurrió un error crítico al crear la tarea.")

        return False

# --- Función mostrar tareas ---

def show_tasks(task_list):
    print(B + "\n------ TAREAS REGISTRADAS ------\n" + RA)
    if not task_list:
        print(Y + "No hay tareas registradas." + RA)
    else:
        tasks(task_list)

# --- Función eliminar tareas ---        

def delete_task(task_list):
    print(B + "\n------ ELIMINAR TAREA ------\n" + RA)
    if not task_list:
        print(Y + "No hay tareas registradas." + RA)
        return False
    else:
        tasks(task_list)

    while True:
        try:
            seleccion = input(Y + "\nIntroduce el número de la tarea que deseas eliminar: " + RA).strip()
            tasks(task_list)
            numero = int(seleccion)

            # Intentamos acceder por índice (se resta -1 porque empieza en 0)
            tarea_eliminada = task_list.pop(numero - 1)
            print(f"\nTarea {G}'{tarea_eliminada.title}'{RA} {R}eliminada{RA} con éxito.")
            logging.info(f"Tarea eliminada con éxito: {tarea_eliminada.title}")
            return True

        except (ValueError, IndexError):
            print(R + "\n■ Error: El número de la tarea no existe." + RA)
            logging.error("Intento de eliminar tarea fallido: Número de tarea inválido.")