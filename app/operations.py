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

        nombre = input(Y + "·Nombre de la tarea: " + RA).strip().capitalize()
        
        while nombre == "":
            print(R + "\n■ Error: El nombre no puede estar vacío.\n")
            logging.error("Nombre inválido. Intentando ingresar un nombre vacíos.")
            nombre = input(Y + "Nombre de la tarea: " + RA).strip().capitalize()

        description = input(Y + "·Descripción" + RA + " [Opcional]: ").strip()
        priority = input(Y + "·Prioridad (Alta, Media, Baja)" + RA + " [Opcional]: ").strip().lower()

        # Mientras no este vacía y no sea una prio del array, pedir de nuevo
        while (priority != "") and (priority not in ("alta", "media", "baja")):
            print(R + "\n■ Error: Prioridad no válida.\n")
            logging.error(f"Prioridad inválida. Intendando ingresar '{priority}' como prioridad.")
            priority = input(Y + "·Prioridad (Alta, Media, Baja)" + RA + " [Opcional]: ").strip().lower()

        kwargs = {}
        if description:
            kwargs["description"] = description
        if priority:
            kwargs["priority"] = priority.capitalize()

        # Se le pasan los argumentos al constructor para hacer un nuevo objeto
        nueva_tarea = To_do(
            title=nombre,
            **kwargs
        )

        task_list.append(nueva_tarea)
        print(f"{G}\nTarea '{nombre}' añadida con éxito.{RA}")
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
            seleccion = input(Y + "\n·Introduce el número de la tarea que deseas eliminar: " + RA).strip()
            tasks(task_list)
            number = int(seleccion)

            # Intentamos acceder por índice (se resta -1 porque empieza en 0)
            tarea_eliminada = task_list.pop(number - 1)
            print(f"\nTarea {G}'{tarea_eliminada.title}'{RA} {R}eliminada{RA} con éxito.")
            logging.info(f"Tarea eliminada con éxito: {tarea_eliminada.title}")
            return True

        except (ValueError, IndexError):
            print(R + "\n■ Error: El número de la tarea no existe." + RA)
            logging.error("Intento de eliminar tarea fallido: Número de tarea inválido.")


# --- Función modificar tareas ---

def edit_task(task_list):
    print(B + "\n------ EDITAR TAREA ------\n" + RA)
    if not task_list:
        print(Y + "No hay tareas registradas." + RA)
        return False

    for indice, task in enumerate(task_list, 1):
        print(f"{G}{indice}. {RA}{task}")

    while True:
        try:
            seleccion = input(Y + "\n·Introduce el número de la tarea que deseas editar (o 'S' para salir): " + RA).strip()
            
            if seleccion.lower() == 's' or seleccion == "" or seleccion.lower() == "salir":
                print(Y + "\n---Operación cancelada---" + RA)
                return False

            # Intentamos acceder por índice (se resta -1 porque empieza en 0)(Misma lógica que en delete_task)
            number = int(seleccion)
            tarea = task_list[number - 1]
            break

        except (ValueError, IndexError):
            print(R + "\n■ Error: El número de la tarea no existe. Inténtalo de nuevo." + RA)

    print(B + f"\nEditando tarea: {tarea.title}\n" + RA)
    print("Deja el campo vacío y presiona " + Y + "Enter ↵" + RA + " si no deseas modificarlo.\n")

    new_name = input(Y + f"·Nuevo nombre {G}[{tarea.title}]: " + RA).strip()
    if new_name:
        tarea.title = new_name.capitalize()

    new_description = input(Y + f"·Nueva descripción {G}[{tarea.description}]: " + RA).strip()
    if new_description:
        tarea.description = new_description
        tarea.description_original = new_description

    new_priority = input(Y + f"·Nueva prioridad (Alta, Media, Baja) {RA}{G}[{tarea.priority}]: " + RA).strip().lower()
    while (new_priority != "") and (new_priority not in ("alta", "media", "baja")):
        print(R + "\n■ Error: Prioridad no válida.\n")
        new_priority = input(Y + "·Nueva prioridad (Alta, Media, Baja): " + RA).strip().lower()

    if new_priority:
        tarea.priority = new_priority.capitalize()

    print(G + f"\nTarea actualizada con éxito." + RA)
    logging.info(f"Tarea editada con éxito: {tarea.title}")
    return True